from flask import Blueprint, request, jsonify, current_app
from adapters.flask_api.inputs.agent_input import AgentForm
from shared.utils.exceptions import NotFoundModel, UniqueViolation


agent_blueprint = Blueprint("agent_blueprint", __name__)
dependencies = lambda dependencie: getattr(
    current_app.blueprints["agent_blueprint"].dependencie_container, dependencie
)


@agent_blueprint.route("/agents", methods=["GET"])
def get_agents():
    """
    Retrieve all agents.

    Returns:
        A JSON response containing a list of agents and a message.
    """
    agent_service = dependencies("service_agent")
    localization = dependencies("localization")
    agents = agent_service.find_all_agents()
    return (
        jsonify(
            agents=[agent.to_dict() for agent in agents],
            message=localization.get_message("agent_read"),
        ),
        200,
    )


@agent_blueprint.route("/agents/<string:identifier>", methods=["GET"])
def get_agent(identifier):
    """
    Retrieve a agent by identifier.

    Args:
        identifier (str): The identifier of the agent.

    Returns:
        A JSON response containing the agent and a message.

    Raises:
        NotFoundModel: If the agent is not found.
    """
    agent_service = dependencies("service_agent")
    localization = dependencies("localization")
    try:
        agent = agent_service.find_agent_by_identifier(identifier)
        return (
            jsonify(agent=agent.to_dict(), message=localization.get_message("agent_read")),
            200,
        )
    except NotFoundModel:
        return jsonify(agent={}, message=localization.get_message("agent_not_found"))


@agent_blueprint.route("/agents", methods=["POST"])
def register_agent():
    """
    Register a new agent.

    Returns:
        A JSON response containing the created agent and a message.

    Raises:
        UniqueViolation: If the agent already exists.
    """
    agent_service = dependencies("service_agent")
    localization = dependencies("localization")
    form = AgentForm(formdata=request.form, data=request.get_json())
    if not form.validate():
        return jsonify(agent={}, message=form.errors), 400
    try:
        agent = agent_service.register_agent(form.name.data, form.identifier.data)
        return (
            jsonify(
                agent=agent.to_dict(), message=localization.get_message("agent_created")
            ),
            200,
        )
    except UniqueViolation as e:
        return jsonify(agent={}, message=localization.get_message("agent_exists")), 409


@agent_blueprint.route("/agents", methods=["PUT"])
def update_agent():
    """
    Update a agent.

    Returns:
        A JSON response containing the updated agent and a message.

    Raises:
        NotFoundModel: If the agent is not found.
    """
    agent_service = dependencies("service_agent")
    localization = dependencies("localization")
    form = AgentForm(formdata=request.form, data=request.get_json())
    if not form.validate():
        return jsonify(agent={}, message=form.errors), 400
    try:
        agent = agent_service.update_agent(form.name.data, form.identifier.data)
        return jsonify(
            agent=agent.to_dict(), message=localization.get_message("agent_updated")
        )
    except NotFoundModel:
        return jsonify(agent={}, message=localization.get_message("agent_not_found")), 404


@agent_blueprint.route("/agents/<string:identifier>", methods=["DELETE"])
def delete_agent(identifier):
    """
    Delete a agent by identifier.

    Args:
        identifier (str): The identifier of the agent to delete.

    Returns:
        A JSON response containing a message.

    Raises:
        NotFoundModel: If the agent is not found.
    """
    agent_service = dependencies("service_agent")
    localization = dependencies("localization")
    try:
        agent_service.remove_agent(identifier)
        return jsonify(agent={}, message=localization.get_message("agent_deleted")), 200
    except NotFoundModel:
        return jsonify(agent={}, message=localization.get_message("agent_not_found")), 404

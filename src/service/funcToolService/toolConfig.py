from __future__ import annotations

from constants import ToolCategory

CATEGORY_CONFIG: dict[str, ToolCategory] = {
    # Local tools
    "get_time": ToolCategory.READ,
    "get_dept_info": ToolCategory.READ,
    "get_room_info": ToolCategory.READ,
    "get_agent_info": ToolCategory.READ,
    "wake_up_agent": ToolCategory.BASIC,
    "send_chat_msg": ToolCategory.BASIC,
    "finish_chat_turn": ToolCategory.BASIC,
    "list_role_templates": ToolCategory.ADMIN,
    "get_role_template": ToolCategory.ADMIN,
    "save_role_template": ToolCategory.ADMIN,
    "delete_role_template": ToolCategory.ADMIN,
    # TSP tools
    "list_dir": ToolCategory.READ,
    "read_file": ToolCategory.READ,
    "write_file": ToolCategory.WRITE,
    "edit": ToolCategory.WRITE,
    "grep_search": ToolCategory.READ,
    "glob": ToolCategory.READ,
    "execute_bash": ToolCategory.EXECUTE,
    "process_output": ToolCategory.EXECUTE,
    "process_stop": ToolCategory.EXECUTE,
    "process_list": ToolCategory.EXECUTE,
}

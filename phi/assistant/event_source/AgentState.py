from enum import Enum


class AgentStateEnum(Enum):
    RECEIVED = "prompt received from user"
    PROCESSING_PROMPT = "llm processing_prompt"
    RESPONDED = "agent responded"
    AGENT_RECEIVED_LLM_RESPONSE = "received_llm_response"
    RECEIVED_LLM_RESPONSE = "rec_llm_response"
    ERROR = "error"
    
"""Represents a connection response message under RFC 23 (DID exchange)."""

from marshmallow import EXCLUDE, fields

from .....messaging.agent_message import AgentMessage, AgentMessageSchema
from .....messaging.decorators.attach_decorator import (
    AttachDecoratorData,
    AttachDecoratorDataSchema,
)

from ..message_types import CONN23_RESPONSE, PROTOCOL_PACKAGE

HANDLER_CLASS = f"{PROTOCOL_PACKAGE}.handlers.response_handler.Conn23ResponseHandler"


class Conn23Response(AgentMessage):
    """Class representing a connection response under RFC 23 (DID exchange)."""

    class Meta:
        """Metadata for a connection response under RFC 23 (DID exchange)."""

        handler_class = HANDLER_CLASS
        message_type = CONN23_RESPONSE
        schema_class = "Conn23ResponseSchema"

    def __init__(
        self,
        *,
        did: str = None,
        did_doc_attach: AttachDecoratorData = None,
        **kwargs,
    ):
        """
        Initialize connection response object under RFC 23 (DID exchange).

        Args:
            image_url: Optional image URL for this connection response
            did_doc_attach: signed DID doc attachment
        """
        super().__init__(**kwargs)
        self.did = did
        self.did_doc_attach = did_doc_attach


class Conn23ResponseSchema(AgentMessageSchema):
    """Schema class for connection response under RFC 23 (DID exchange)."""

    class Meta:
        """DID exchange connection response schema class metadata."""

        model_class = DIDExResponse
        signed_fields = ["did_doc_attach"]
        unknown = EXCLUDE

    did = fields.Str(description="DID of exchange", **INDY_DID)
    did_doc_attach = fields.Nested(
        AttachDecoratorDataSchema,
        required=False,
        description="DID Doc associated with DID as signed attachment",
        data_key="did_doc~attach",
    )

from pydantic import BaseModel

class PropertyDefinition(BaseModel):

    type: Literal[
        "string",
        "integer",
        "number",
        "boolean",
        "array",
        "object",
    ]

    description: str | None = None

class ParameterDefinition(BaseModel):

    type: Literal["object"]

    properties: dict[str, PropertyDefinition]

    required: list[str]

    @model_validator(mode="after")
        def validate_required(self):

            for field in self.required:

                if field not in self.properties:
                    raise ValueError(
                        f"'{field}' is required but is not defined in properties."
                    )

            return self
            
class ToolDefinition(BaseModel):
    name: str
    description: str
    parameters: ParameterDefinition

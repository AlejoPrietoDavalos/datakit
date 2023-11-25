from .fn_act import FnActHandler, FnActEnum
from pydantic import BaseModel, Field

__all__ = ["CfgModule"]

class CfgModule(BaseModel):
    fn_act_name: FnActEnum = Field(default=FnActEnum.RELU.value)
    fn_act_args: dict = Field(default_factory=dict)
    
    @property
    def fn_act(self):
        return FnActHandler.get_fn_act(self.fn_act_name, self.fn_act_args)

    class Config:  
        use_enum_values = True

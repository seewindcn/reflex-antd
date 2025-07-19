from typing import Optional, Union, Any
import reflex as rx
from reflex.constants import EventTriggers
from reflex import Component, Var
from reflex.utils.imports import ImportDict, ImportVar, ParsedImportDict
from reflex_antd import helper


# *** v4.23.9开始, package.json中增加了 type: "module" 配置 ***
# 会引起页面刷新报错, 具体看 README.md
VERSION = '@4.23.8'
lib_dependencies: list[str] = [
    f'@uiw/codemirror-extensions-basic-setup{VERSION}',
    f'@uiw/codemirror-theme-okaidia{VERSION}',
]


class CodeMirror(rx.Component):
    """ https://github.com/uiwjs/react-codemirror

    # 需要转义成类似如下内容
    import CodeMirror from '@uiw/react-codemirror';
    import { yaml } from '@codemirror/lang-yaml';
    import { okaidia } from '@uiw/codemirror-theme-okaidia';

    const extensions = [javascript({ jsx: true })];

    export default function App() {
        return (
            <CodeMirror
            value="console.log('hello world!');"
            height="200px"
            theme={okaidia}
            extensions={extensions}
            />
        );
    }
    """
    library = f'@uiw/react-codemirror{VERSION}'
    tag = 'CodeMirror'
    lib_dependencies: list[str] = lib_dependencies
    is_default = True

    value: Var[str]
    height: Var[Union[str, int]]  # auto|高
    width: Var[Union[str, int]]  # auto|宽
    theme: Var[Any]
    extensions: Var[list]
    read_only: Var[bool]

    def get_event_triggers(self) -> dict[str, Any]:
        _triggers = super().get_event_triggers()
        _triggers.update({
            EventTriggers.ON_CHANGE: lambda val, view: [val],
        })
        return _triggers

    def _get_style(self) -> dict:
        return {}
        # return {"style": self.style}

    def _get_imports(self) -> ParsedImportDict:
        _imports = {
            f'@uiw/codemirror-theme-okaidia{VERSION}': [
                ImportVar(tag='okaidia', is_default=False, alias=None, install=True, render=True)
            ],
            f'@uiw/react-codemirror{VERSION}': [
                ImportVar(tag='CodeMirror', is_default=True, alias=None, install=True, render=True)
            ]
        }
        return _imports


class YamlEdit(CodeMirror):
    """ """
    lib_dependencies: list[str] = ['@codemirror/lang-yaml'] + lib_dependencies

    @classmethod
    def create(cls, *children, **props) -> Component:
        rs = super().create(*children, **props)
        rs.extensions = helper.casual_var('[yaml({ jsx: true })]', _var_type=list)
        return rs

    def _get_imports(self) -> ParsedImportDict:
        _imports = super()._get_imports()
        _imports.update(
            {
                '@codemirror/lang-yaml': [
                    ImportVar(tag='yaml', is_default=False, alias=None, install=True, render=True)
                ],
            }
        )
        return _imports

    # def _get_hooks(self) -> str | None:
    #     return 'const extensions = [yaml({ jsx: true })];'


class JsonEdit(CodeMirror):
    lib_dependencies: list[str] = ['@codemirror/lang-json'] + lib_dependencies

    @classmethod
    def create(cls, *children, **props) -> Component:
        rs = super().create(*children, **props)
        rs.extensions = helper.casual_var('[json({ jsx: true })]', _var_type=list)
        return rs

    def _get_imports(self) -> ParsedImportDict:
        _imports = super()._get_imports()
        _imports.update(
            {
                '@codemirror/lang-json': [
                    ImportVar(tag='json', is_default=False, alias=None, install=True, render=True)
                ],
            }
        )
        return _imports

    # def _get_hooks(self) -> str | None:
    #     return 'const extensions = [json({ jsx: true })];'


class PythonEdit(CodeMirror):
    lib_dependencies: list[str] = ['@codemirror/lang-python'] + lib_dependencies

    @classmethod
    def create(cls, *children, **props) -> Component:
        rs = super().create(*children, **props)
        rs.extensions = helper.casual_var('[python()]', _var_type=list)
        return rs

    def _get_imports(self) -> ParsedImportDict:
        _imports = super()._get_imports()
        _imports.update(
            {
                '@codemirror/lang-python': [
                    ImportVar(tag='python', is_default=False, alias=None, install=True, render=True)
                ],
            }
        )
        return _imports


yaml_edit = YamlEdit.create
json_edit = JsonEdit.create
python_edit = PythonEdit.create


def test_yaml_edit() -> None:
    return yaml_edit(
        height='300px',
        theme=helper.casual_var('okaidia'),
        extensions=helper.casual_var('extensions', _var_type=list),
        read_only=True,
    )

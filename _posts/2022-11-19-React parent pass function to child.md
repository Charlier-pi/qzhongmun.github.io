## Class redux read data and import updatafunction

### parent

```
import { Msddbox } from "../utils/Msddbox";

export const Multfone = (props) => {
  const [zaxis, setZaxis] = React.useState("well1");

  const handleChangez = (event) => {
    setZaxis(event.target.value);
    // zaxis = event.target.value;
    //console.log(zaxis);
  };


  return (
      <CardHeader
        titlestyle={{ paddingRight: 0, marginRight: 0, width: 200 }}
        // style={{ margin: "0px", paddingLeft: "0px" }}
        title={
          <div
            style={{
              // fontSize: 16,
              width: 200,
              padding: 0,
              margin: 0,
            }}
          >
            Damage Detection
          </div>
          // span
        }
        action={
          <>
              <Msddbox
                label={"well"}
                axis={zaxis}
                default={"well1"}
                lists={["well2"]}
                handleClick={handleChangez}
              />
          </>
        }
      />
  );
};
```

### child

```
import * as React from "react";
import MenuItem from "@mui/material/MenuItem";
import InputLabel from "@mui/material/InputLabel";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";

export const Msddbox = (props) => {
  function AddMenuItem() {
    var a = [];
    if (props.lists) {
      for (var i = 0; i < props.lists.length; i++) {
        a.push(
          <MenuItem key={i} value={props.lists[i]}>
            {props.lists[i]}
          </MenuItem>
        );
      }
    }
    return a;
  }

  const MenuProps = {
    PaperProps: {
      style: {
        maxHeight: 260,
      },
    },
  };

  // console.log("style", props.style);
  return (
    <FormControl
      sx={{ m: 1, minWidth: 85, maxWidth: 95, marginLeft: props.style }}
      size="small"
      variant="outlined"
      color="secondary"
    >
      <InputLabel id="demo-select-small">{props.label}</InputLabel>
      <Select
        labelId="demo-select-small"
        id="demo-select-small"
        value={props.axis}
        label={props.axis}
        onChange={props.handleClick}
        MenuProps={MenuProps}
      >
        <MenuItem value={props.default}>
          <em>{props.default}</em>
        </MenuItem>
        {AddMenuItem()}
      </Select>
    </FormControl>
  );
};

```

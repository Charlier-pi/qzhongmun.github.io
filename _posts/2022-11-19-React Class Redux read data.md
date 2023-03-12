## Class redux read data and import updatafunction

```
import React, { Component } from "react";
import { useSelector } from "react-redux";
import { connect } from "react-redux";
import { UpdateData } from "../../redux/counter";

class Multifone extends Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() {
    // var { t9307, t9302 } = useSelector((state) => state.counter);

    var data02 = this.props.count.t9302;
    var data07 = this.props.count.t9307;
    //console.log("data1", data1);

    var root = am5.Root.new("chartdiv4");
    root._logo.dispose();


    chart.appear(1000, 100);

    this.root = root;
  }

  componentWillUnmount() {
    if (this.root) {
      this.root.dispose();
    }
  }

  render() {
    return (
      <div id="chartdiv4" style={{ width: "100%", height: "500px" }}></div>
    );
  }
}

function mapStateToProps(state) {
  return { count: state.counter };
}

export default connect(mapStateToProps, { UpdateData })(Multifone);

```

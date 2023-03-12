### Convert Class Component to Function Component

## Class Component
'''

import React, { Component } from "react";
import * as am5 from "@amcharts/amcharts5";
import * as am5xy from "@amcharts/amcharts5/xy";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5map from "@amcharts/amcharts5/map";

import { connect } from "react-redux";
import { UpdateData } from "../../redux/counter";

class Verticalchart1 extends Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() {
    var root = am5.Root.new("chartdiv6");
    root._logo.dispose();

    chart.appear(1000, 100);
    this.root = root;
  }

  componentDidUpdate(oldProps) {
    if (
      (oldProps.xaxises !== this.props.xaxises) |
      (oldProps.yaxis !== this.props.yaxis) |
      (oldProps.wellname !== this.props.wellname)
    ) {
    }
  }

  componentWillUnmount() {
    if (this.root) {
      this.root.dispose();
    }

    clearInterval(this.timer);
  }

  render() {
    return (
      <div id="chartdiv6" style={{ width: "100%", height: "650px" }}></div>
    );
  }
}

function mapStateToProps(state) {
  return { count: state.counter };
}

export default connect(mapStateToProps, { UpdateData })(Verticalchart1);


'''

## Function Component
'''

import React, { Component } from "react";
import * as am5 from "@amcharts/amcharts5";
import * as am5xy from "@amcharts/amcharts5/xy";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5map from "@amcharts/amcharts5/map";
import { useDispatch, useSelector } from "react-redux";

export default function Verticalchart1(props) {
  const { count } = useSelector((state) => state.counter);
  const dispatch = useDispatch();

  useEffect(() => {
    var root = am5.Root.new("chartdiv6");
    root._logo.dispose();
    // Set themes
    // https://www.amcharts.com/docs/v5/concepts/themes/
    root.setThemes([am5themes_Animated.new(root)]);

    chart.appear(1000, 100);
    // Make stuff animate on load
    // https://www.amcharts.com/docs/v5/concepts/animations/

    root.current = root;
    return () => {
      root.dispose();
    };
  }, [props]);

  return <div id="chartdiv6" style={{ width: "100%", height: "650px" }}></div>;
}


'''

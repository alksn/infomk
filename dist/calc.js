"use strict";

function _instanceof(left, right) { if (right != null && typeof Symbol !== "undefined" && right[Symbol.hasInstance]) { return !!right[Symbol.hasInstance](left); } else { return left instanceof right; } }

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function _classCallCheck(instance, Constructor) { if (!_instanceof(instance, Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } return _assertThisInitialized(self); }

function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }

function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); if (superClass) _setPrototypeOf(subClass, superClass); }

function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf || function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }

var Calc =
/*#__PURE__*/
function (_React$Component) {
  _inherits(Calc, _React$Component);

  function Calc(props) {
    var _this;

    _classCallCheck(this, Calc);

    _this = _possibleConstructorReturn(this, _getPrototypeOf(Calc).call(this, props));
    _this.handleClick = _this.handleClick.bind(_assertThisInitialized(_this));
    var v_num = parseInt($("#v_num").val());
    var win = parseInt($("#label_win").text());
    var lose = parseInt($("#label_lose").text());
    var avg_sfr = parseFloat($("#label_sfr").text());
    var bet = 100;

    var dogon = _this.dogon(v_num, avg_sfr, bet);

    _this.state = {
      date: new Date(),
      info: document.getElementById('r_limit').value,
      info2: $("#r_limit").val(),
      win: win,
      lose: lose,
      avg_sfr: avg_sfr,
      v_num: v_num,
      num_k: _this.dogon(v_num, avg_sfr, bet),
      num_n: bet,
      rez: _this.formula(win, lose, dogon, avg_sfr, bet) // 4392.23 =)

    };
    return _this;
  } //(8141*(2.811*N-N))-1859*K


  _createClass(Calc, [{
    key: "formula",
    value: function formula(win, lose, dogon, sfr, bet) {
      var foo = win * (sfr * bet - bet) - lose * dogon;
      return foo.toFixed(2);
    }
  }, {
    key: "dogon",
    value: function dogon(rounds) {
      var sfr = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 2.811;
      var bet = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : 100;
      var k = parseFloat(sfr);
      var foo = 0;
      var sum = parseFloat(bet);
      var sum2 = 0;
      var i = 1;

      while (i <= rounds) {
        sum2 += sum;
        foo = sum / (k - 1);
        sum += foo;
        i++;
      }

      ;
      return sum2.toFixed(2);
    }
  }, {
    key: "handleClick",
    value: function handleClick(event) {
      //console.log('this is:', this, event.target);
      var k = 10 / event.target.value;
      var name = event.target.name;
      this.setState(_defineProperty({}, name, event.target.value));
      var win = this.state.win;
      var lose = this.state.lose;
      var sfr = this.state.avg_sfr;
      var bet = this.state.num_n;
      var v_num = this.state.v_num;
      if (name == 'win') win = event.target.value;
      if (name == 'lose') lose = event.target.value;
      if (name == 'avg_sfr') sfr = event.target.value;
      if (name == 'num_n') bet = event.target.value;
      var dogon = this.dogon(v_num, sfr, bet);
      if (name == 'num_k') dogon = event.target.value;else this.setState({
        num_k: dogon
      });
      k = this.formula(win, lose, dogon, sfr, bet);
      this.setState(function (state) {
        return {
          rez: k
        };
      });
    }
  }, {
    key: "render",
    value: function render() {
      var element = React.createElement("div", {
        className: "accordion"
      }, React.createElement("div", {
        className: ""
      }, React.createElement("div", {
        className: ""
      }, React.createElement("div", {
        className: "card"
      }, React.createElement("div", {
        className: "card-header text-center"
      }, React.createElement("a", {
        href: "#calc-collapse",
        "data-toggle": "collapse"
      }, "\u041A\u0430\u043B\u044C\u043A\u0443\u043B\u044F\u0442\u043E\u0440")), React.createElement("div", {
        id: "calc-collapse",
        className: "collapse show"
      }, React.createElement("div", {
        className: "card-body"
      }, React.createElement("div", {
        className: "row"
      }, React.createElement("div", {
        className: "col-sm align-self-center text-right"
      }, "\u0423\u0441\u043F\u0435\u0448\u043D\u044B\u0445 \u0441\u0442\u0430\u0432\u043E\u043A:"), React.createElement("div", {
        className: "col-sm align-self-center"
      }, React.createElement("input", {
        type: "text",
        className: "form-control",
        id: "win",
        name: "win",
        defaultValue: this.state.win,
        onChange: this.handleClick,
        placeholder: ""
      }))), React.createElement("div", {
        className: "row my-1"
      }, React.createElement("div", {
        className: "col-sm align-self-center text-right"
      }, "\u041F\u0440\u043E\u0438\u0433\u0440\u044B\u0448\u0435\u0439:"), React.createElement("div", {
        className: "col-sm align-self-center"
      }, React.createElement("input", {
        type: "text",
        className: "form-control",
        id: "lose",
        name: "lose",
        defaultValue: this.state.lose,
        onChange: this.handleClick,
        placeholder: ""
      }))), React.createElement("div", {
        className: "row my-1"
      }, React.createElement("div", {
        className: "col-sm align-self-center text-right"
      }, "\u041A\u043E\u044D\u0444\u0444\u0438\u0446\u0438\u0435\u043D\u0442:"), React.createElement("div", {
        className: "col-sm align-self-center"
      }, React.createElement("input", {
        type: "text",
        className: "form-control",
        id: "avg_sfr",
        name: "avg_sfr",
        defaultValue: this.state.avg_sfr,
        onChange: this.handleClick,
        placeholder: ""
      }))), React.createElement("div", {
        className: "row my-1"
      }, React.createElement("div", {
        className: "col-sm align-self-center text-right"
      }, "K:"), React.createElement("div", {
        className: "col-sm align-self-center"
      }, React.createElement("input", {
        type: "text",
        className: "form-control",
        id: "num_k",
        name: "num_k",
        value: this.state.num_k,
        onChange: this.handleClick,
        placeholder: ""
      }))), React.createElement("div", {
        className: "row"
      }, React.createElement("div", {
        className: "col-sm align-self-center text-right"
      }, "N:"), React.createElement("div", {
        className: "col-sm align-self-center"
      }, React.createElement("input", {
        type: "text",
        className: "form-control",
        id: "num_n",
        name: "num_n",
        defaultValue: this.state.num_n,
        onChange: this.handleClick,
        placeholder: ""
      })))), React.createElement("div", {
        className: "card-footer"
      }, React.createElement("div", {
        className: "row"
      }, React.createElement("div", {
        className: "col-sm align-self-center text-right"
      }, "\u0420\u0435\u0437\u0443\u043B\u044C\u0442\u0430\u0442:"), React.createElement("div", {
        className: "col-sm align-self-center"
      }, this.state.rez))))))));
      return React.createElement("div", null, element);
    }
  }]);

  return Calc;
}(React.Component);

ReactDOM.render(React.createElement(Calc, {
  element: "\u043F\u0443\u0441\u0442\u0430\u044F \u0441\u0442\u0440\u043E\u043A\u0430"
}), document.getElementById('calc'));
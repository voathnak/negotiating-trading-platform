import React, { Component, useState, useEffect } from "react";
import { Link } from "react-router-dom";

import EditableLabel from "./Components/editableLabel";
import { Row, Col } from "antd";
import "./Profile.css";
import { useDispatch, useSelector } from "react-redux";
import { balanceActions } from "../_actions";
import { balanceService } from "../_services";
import Loader from "react-loader-spinner";

const Profile = () => {
  const [isBusy, setBusy] = useState(true);
  const [busyField, setBusyField] = useState([]);
  const [balance, setBalance] = useState({});
  const user = useSelector((state) => state.authentication.user);
  const dispatch = useDispatch();

  // const [labelCash, setLabelCash] = useState('20000');
  useEffect(() => {
    const balanceRequest = balanceService.getAll();
    // dispatch(balanceActions.getAllBalance());
    balanceRequest.then((balance) => {
      console.log({ balance });
      setBalance(balance);
      setBusy(false);
    });
    // Clean Up
    return () => {
      // setBalance({});
    };
  }, []);

  const changeLabelEvent = (updatedBalance) => {
    console.log("changeLabelEvent", { balance });
    console.log({ newValue: updatedBalance });
    if (Object.keys(updatedBalance)[0] === "cash_balance") {
      Object.assign(balance, updatedBalance);
    } else {
      Object.assign(balance.stock_balance, updatedBalance);
    }
    setBusyField([...busyField, Object.keys(updatedBalance)[0]]);
    console.log(2, balance);
    const updatedBalancePromise = balanceService.updateAll(balance);
    updatedBalancePromise.then((balance) => {
      setBalance(balance);
      setBusyField(
        busyField.splice(busyField.indexOf(Object.keys(updatedBalance)[0]), 1)
      );
    });
    // dispatch(balanceActions.updateBalance(newValue));
  };

  return !isBusy ? (
    <div className="container">
      <div className="left-container">
        <img
          className="image"
          alt="test"
          src="https://i1.pngguru.com/preview/137/834/449/cartoon-cartoon-character-avatar-drawing-film-ecommerce-facial-expression-png-clipart.jpg"
        />
        <p>{user.email}</p>
        <p>
          <Link
            to="/login"
            onClick={() => {
              location.reload(true);
            }}
          >
            Logout
          </Link>
        </p>
      </div>
      <div className="right-container">
        <Row key={"cash_balance"}>
          <Col className="labelTitle">
            <p> Cash Balance </p>
          </Col>
          {balance && (
            <Col>
              {busyField.indexOf("cash_balance") == -1 ? (
                <EditableLabel
                  dataKey={"cash_balance"}
                  labelValue={balance.cash_balance.toString()}
                  editChangeEvent={changeLabelEvent}
                />
              ) : (
                <Loader
                  type="TailSpin"
                  color="#00BFFF"
                  height={20}
                  width={20}
                />
              )}
            </Col>
          )}
        </Row>
        <Row className="labelTitle">
          <p>Securities Balance</p>
        </Row>
        {balance &&
          Object.entries(balance.stock_balance).map((x) => (
            <Row key={x[0]}>
              <Col className="subTitle">
                <p>{x[0]}</p>
              </Col>
              <Col className="editable-label">
                {busyField.indexOf(x[0]) == -1 ? (
                  <EditableLabel
                    dataKey={x[0]}
                    labelValue={x[1].toString()}
                    editChangeEvent={changeLabelEvent}
                  />
                ) : (
                  <Loader
                    type="TailSpin"
                    color="#00BFFF"
                    height={20}
                    width={20}
                  />
                )}
              </Col>
            </Row>
          ))}
      </div>
    </div>
  ) : (
    <div className="loading-container">
      <Loader type="TailSpin" color="#00BFFF" height={100} width={100} />
    </div>
  );
};

export default Profile;

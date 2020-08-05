import { Table, Button } from 'antd';
import React, { useState, useEffect } from 'react';
import Loader from "react-loader-spinner";
import 'antd/dist/antd.css';
import MyForm from './Components/AntForm';
import EditableRowTable from './Components/EditableRowTable';
import { orderService } from "../_services";


const TableOrder = () => {

  const [isShowForm, setIsShowForm] = useState(false);
  const [isShowTable, setIsShowTable] = useState(true);
  const [orderData, setOrderData] = useState(true);
  const [isBusy, setBusy] = useState(true);
  const [orderVersion, updateOrderVersion] = useState(0);


  const handleDisplayToggle = () => {
    setIsShowForm(!isShowForm);
    setIsShowTable(!isShowTable);

  };

  useEffect(() => {
    const orderLoadingPromised = orderService.getAll();

    orderLoadingPromised.then((data) => {
      console.log("orders", data.orders);
      const unusedKey = ['createdAt', 'itemId', 'updatedAt', 'username'];

      const orderData = data.orders.map((x) => {
        Object.assign(x, {key: x.itemId, status: 'pending'});
        unusedKey.map((name) => delete x[name]);
        return x;
      });
      setOrderData(orderData);
      setBusy(false);
    });
    // Clean Up
    return () => {

    };
  }, [orderVersion]);

  const placeOrderFormSubmit = (values) => {
    console.log("# 1364 #", values);
    const orderCreationPromised = orderService.create(values);
    orderCreationPromised.then( order => {
      console.log("created order:", order);
      updateOrderVersion(orderVersion + 1);
      handleDisplayToggle();
    });


  };

  const handleCancelBtn = () => {
    return (
      <>
      <Button type="primary" htmlType="submit" onClick={handleDisplayToggle}>
        Cancel
      </Button>
      <MyForm onSubmit={placeOrderFormSubmit} />
      </>
    );
  };


  const handleCreateBtn = () => {
    return (
      <>
      <Button type="primary" htmlType="submit" onClick={handleDisplayToggle}>
        Place Order
      </Button>
      {!isBusy ? (<EditableRowTable data={orderData} />) : (
        <div className="loading-container">
          <Loader type="TailSpin" color="#00BFFF" height={100} width={100}/>
        </div>
      )}
      </>
    );
  };
    return (isShowForm ? handleCancelBtn() : handleCreateBtn());
};

export default TableOrder;

import { Form, Input, Button, Select } from 'antd';
import React from 'react';
import 'antd/dist/antd.css';
import PropTypes from 'prop-types';

const { Option } = Select;
const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 8,
  },
};
const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 16,
  },
};

const MyForm = (props) => {
  const [form] = Form.useForm();
  const {onSubmit} = props;

  const onFinish = values => {
    console.log("# 1432 #", values);
    onSubmit(values);
  };

  const onReset = () => {
    form.resetFields();
  };

  const onFill = () => {
    form.setFieldsValue({
      stock: 'PPSP',
      type: 'buy',
      price: 10,
      quantity: 10
    });
  };

  return (
    <Form {...layout} form={form} name="control-hooks" onFinish={onFinish}>
      <Form.Item
        name="stock"
        label="Stock"
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Select
          placeholder="Select a option"
          allowClear
        >
          <Option value="PPAP">PPAP</Option>
          <Option value="GTI">GTI</Option>
          <Option value="PAS">PAS</Option>
          <Option value="PWSA">PWSA</Option>
          <Option value="PPSP">PPSP</Option>
          <Option value="ABC">ABC</Option>
        </Select>
      </Form.Item>
      <Form.Item
        name="type"
        label="Order Type"
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Select
          placeholder="Select a type"
          allowClear
        >
          <Option value="buy">Buy</Option>
          <Option value="sell">Sell</Option>
        </Select>
      </Form.Item>

      <Form.Item
        name="price"
        label="Price"
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        name="quantity"
        label="Quantity"
        rules={[
          {
            required: true,
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item {...tailLayout}>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
        <Button htmlType="button" onClick={onReset}>
          Reset
        </Button>
        <Button type="link" htmlType="button" onClick={onFill}>
          Fill form
        </Button>
      </Form.Item>
    </Form>
  );
};

MyForm.propTypes = {
  data: PropTypes.object,
  onSubmit: PropTypes.func
}

MyForm.defaultProps = {
  data: {},
};
export default MyForm;

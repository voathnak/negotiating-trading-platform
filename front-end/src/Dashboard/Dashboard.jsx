import React, { Component } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { Layout, Menu } from "antd";
import "./dashboard.css";
import "antd/dist/antd.css";
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined,
  FileOutlined,
} from "@ant-design/icons";
import Profile from "./Profile";
import TableOrder from "./TableOrder";
import TableRequestOrder from "./TableRequestOrder";
import { LoginPage } from "../LoginPage";

const { Header, Sider, Content } = Layout;

class Dashboard extends React.Component {
  state = {
    collapsed: false,
  };

  toggle = () => {
    this.setState({
      collapsed: !this.state.collapsed,
    });
  };

  render() {
    return (
      <Router>
        <Layout style={{ minHeight: "100vh" }}>
          <Sider trigger={null} collapsible collapsed={this.state.collapsed}>
            <div className="logo" />
            <Menu theme="dark" mode="inline" defaultSelectedKeys={["1"]}>
              <Menu.Item key="1" icon={<UserOutlined />}>
                <span>Profile</span>
                <Link to="/profile" />
              </Menu.Item>
              <Menu.Item key="2" icon={<FileOutlined />}>
                <span>Order</span>
                <Link to="/order" />
              </Menu.Item>
              <Menu.Item key="3" icon={<FileOutlined />}>
                <span>Request Order</span>
                <Link to="/request-order" />
              </Menu.Item>
            </Menu>
          </Sider>

          <Layout className="site-layout">
            <Header className="site-layout-background" style={{ padding: 0 }}>
              {React.createElement(
                this.state.collapsed ? MenuUnfoldOutlined : MenuFoldOutlined,
                {
                  className: "trigger",
                  onClick: this.toggle,
                }
              )}
            </Header>

            <Content
              className="site-layout-background"
              style={{
                margin: "24px 16px",
                padding: 24,
                minHeight: 280,
              }}
            >
              <Route exact path="/profile" component={Profile} />
              <Route path="/order" component={TableOrder} />
              <Route path="/request-order" component={TableRequestOrder} />
            </Content>
          </Layout>
        </Layout>
        <Route exact path="/login" component={LoginPage} />
      </Router>
    );
  }
}

export { Dashboard };

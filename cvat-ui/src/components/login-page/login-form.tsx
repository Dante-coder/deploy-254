// Copyright (C) 2020-2022 Intel Corporation
// Copyright (C) 2022 CVAT.ai Corporation
//
// SPDX-License-Identifier: MIT

import React, { useCallback, useState } from 'react';
import Form from 'antd/lib/form';
import Button from 'antd/lib/button';
import Input from 'antd/lib/input';
import Icon from '@ant-design/icons';
import {
    BackArrowIcon, ClearIcon,
} from 'icons';
import { Col, Row } from 'antd/lib/grid';
import Title from 'antd/lib/typography/Title';
import Text from 'antd/lib/typography/Text';
import { Link } from 'react-router-dom';

export interface LoginData {
    credential: string;
    password: string;
}

interface Props {
    renderResetPassword: boolean;
    fetching: boolean;
    socialAuthentication: JSX.Element | null;
    onSubmit(loginData: LoginData): void;
}

function LoginFormComponent(props: Props): JSX.Element {
    const {
        fetching, onSubmit, renderResetPassword, socialAuthentication,
    } = props;
    const [form] = Form.useForm();
    const [credential, setCredential] = useState('');

    const inputReset = useCallback((name: string):void => {
        form.setFieldsValue({ [name]: '' });
    }, [form]);
    return (
        <div className='cvat-signing-form-wrapper'>
            {
                credential ? (
                    <Row justify='space-between' className='cvat-credentials-navigation'>
                        <Col>
                            <Icon
                                component={BackArrowIcon}
                                onClick={() => {
                                    setCredential('');
                                    form.setFieldsValue({ credential: '' });
                                }}
                            />
                        </Col>
                        {
                            renderResetPassword ? (
                                <Col className='cvat-credentials-link'>
                                    <Text strong>
                                        <Link to={credential.includes('@') ?
                                            `/auth/password/reset?credential=${credential}` : '/auth/password/reset'}
                                        >
                                            Forgot password?
                                        </Link>
                                    </Text>
                                </Col>
                            ) : null
                        }
                    </Row>
                ) : null
            }
            <Row>
                <Col>
                    <Title level={2}> Sign in </Title>
                </Col>
            </Row>
            <Row>
                <Col className='cvat-credentials-link'>
                    <Text strong>
                        New user?&nbsp;
                        <Link to='/auth/register'>Create an account</Link>
                    </Text>
                </Col>
            </Row>
            <Form
                className={`cvat-signing-form
                 ${!credential && !socialAuthentication ? 'cvat-signing-form-empty-socials' : ''}
                 ${credential ? 'cvat-signing-form-extended' : ''}`}
                form={form}
            >
                <Form.Item
                    className='cvat-credentials-form-item'
                    name='credential'
                    rules={[
                        {
                            required: true,
                            message: 'Please specify a email or username',
                        },
                    ]}
                >
                    <Input
                        autoComplete='credential'
                        placeholder='enter your email or username'
                        prefix={<Text>Email or username</Text>}
                        suffix={(
                            credential ? (
                                <Icon
                                    component={ClearIcon}
                                    onClick={() => {
                                        setCredential('');
                                        inputReset('credential');
                                    }}
                                />
                            ) : null
                        )}
                        onChange={(event) => {
                            const { value } = event.target;
                            setCredential(value);
                        }}
                    />
                </Form.Item>
                {
                    credential ? (
                        <Form.Item
                            className='cvat-credentials-form-item'
                            name='password'
                            rules={[
                                {
                                    required: true,
                                    message: 'Please specify a password',
                                },
                            ]}
                        >
                            <Input.Password
                                autoComplete='current-password'
                                placeholder='enter your password'
                                prefix={
                                    <Text>Password</Text>
                                }
                            />
                        </Form.Item>
                    ) : null
                }
            </Form>
            {
                credential || !socialAuthentication ? (
                    <Row>
                        <Col flex='auto'>
                            <Button
                                className='cvat-credentials-action-button'
                                loading={fetching}
                                disabled={!credential}
                                onClick={async () => {
                                    const loginData: LoginData = await form.validateFields();
                                    onSubmit(loginData);
                                }}
                            >
                                Next
                            </Button>
                        </Col>
                    </Row>
                ) : socialAuthentication
            }
        </div>
    );
}

export default React.memo(LoginFormComponent);

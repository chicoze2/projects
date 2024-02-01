import React, {useState} from 'react'
import {
    Box,
    Button,
    Container,
    displayTex,
    onClick,
    handleClick,
    Input,
    InputGroup,
    InputRightElement,
    Stack,
    useProductSearch,
    Radio,
    RadioGroup
} from '@chakra-ui/react'

const MyOptions = () => {
    const [message, setMessage] = React.useState('Change Me')

    

    return (
        <Box align="center">
            <Stack pl={600} pt={20}>
                <RadioGroup onChange={setMessage} value={message}>
                    <Stack direction="row">
                        <Radio value="1">First</Radio>
                        <Radio value="2">Second</Radio>
                        <Radio value="3">Third</Radio>
                    </Stack>
                </RadioGroup>
            </Stack>
        </Box>
    )
}

export default MyOptions

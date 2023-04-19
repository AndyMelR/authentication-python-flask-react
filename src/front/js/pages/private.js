import React, { useEffect, useState} from "react";
import { useNavigate } from "react-router-dom";

const Private = () => {
    const [users, setUsers] = useState()
    const navigate = useNavigate()
useEffect(()=>{
    if (localStorage.getItem("token")) {
        fetch(process.env.BACKEND_URL + "api/private", {
            method: 'GET',
            headers:{
                'Content-Type': 'application/json',
                'Authorization': 'Bearer' + token
            }
        }
        )
        .then ((res => res.json()))
        .then((data)=>{
            if (data.users){
                setUsers(data.users)
                console.log(data)
            }
        })
    }else {
        navigate ("/signup")
    }
},[]);





    return (
        <>
        </>
    )
}
export default Private
import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { Login } from "./login";

export const Home = () => {
	const { store, actions } = useContext(Context);
	const [user, setUser] = useState ({})

	const handleChange = (e) => {
        setUser({...user, [e.target.name]: e.target.value})
	}
	

	return (
	<>
	<div className="container pt-5 m-5">
		<h2 className="title mb-4">SignUp</h2>
		<div className="container m-3">
				<input type="email" placeholder="email" name="email" onChange={handleChange} /> 
				<input type="password" placeholder="password" name="password" onChange={handleChange} />
		</div>
				<button type="button" className="btn btn-success" onClick={() => {
					fetch("https://3001-4geeksacade-reactflaskh-lfhg7jyme0m.ws-eu93.gitpod.io/api/signup",
					{
					method: 'POST', // or 'PUT'
					body: JSON.stringify(user), // data can be `string` or {object}!
					headers:{
						'Content-Type': 'application/json'
					}
					})
					.then(res => res.json())
					.then(response => console.log('Success:', response));
					

				}}>Enviar</button>
	</div>
			<p>
				This boilerplate comes with lots of documentation:{" "}
				<a href="https://start.4geeksacademy.com/starters/react-flask">
					Read documentation
				</a>
			</p>
		
	</>
	);
};



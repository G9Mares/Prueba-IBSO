import { type MetaFunction , type LinksFunction, type LoaderFunctionArgs, type ActionFunctionArgs, broadcastDevReady } from "@remix-run/node";
import styles from "./styles.css?url"
import { Form, useActionData, Link, Outlet } from "@remix-run/react";
import { useFetcher, useLoaderData } from "@remix-run/react";
import { useEffect, useState } from "react";

import { list } from "isbot";

export async function loader(params:LoaderFunctionArgs) {
  const {request} = params
  const url = new URL(request.url)  
  const fecha_search = url.searchParams.get('fecha')
  const requestOptions:RequestInit  = {
    method: "GET",
    redirect: "follow"
  };
  
  const listas = await fetch(`http://127.0.0.1:8000/get_listas`, requestOptions)
    .then((response) => response.json())
    .then((result) => {
      return result
    })
    .catch((error) => console.error(error));
  return {listas:listas}
}

export async function action(params:ActionFunctionArgs){
  console.log("caraculo")
  const {request} = params
  const form = await request.formData()
  const body = Object.fromEntries(form)
  const endpoint = body.endpoint
  delete body.endpoint
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const raw = JSON.stringify(body);
  
  

  const requestOptions:RequestInit  = {
    method: "POST",
    headers: myHeaders,
    body: raw,
    redirect: "follow"

  };
  const respuesta = await fetch(`http://127.0.0.1:8000/${endpoint}`, requestOptions)
    .then((response) => response.json())
    .then((result) => {
      return result
    })
    .catch((error) => console.error(error))
  console.log(respuesta)
  return {libros:respuesta}
}

export const links:LinksFunction = () => [
  {rel:"stylesheet",href:styles}
]
export const meta: MetaFunction = () => {
  return [
    { title: "IBSO - Gustavo Mares" },
    { name: "description", content: "Interfaz NYC API" },
  ];
};

export default function Index() {
  const fetcher= useFetcher()
  const resp = useActionData()
  const {listas} = useLoaderData()
  const [filter,setFilter] = useState()
  const [libros,setLibros] = useState([])
  useEffect(()=>{
    console.log(resp)
    if(!resp) return
    if (resp.libros) {
      console.log(resp.libros)
      setLibros(resp.libros)
    }
  },[resp])
  

  return (
    <>
      <div className="container_header">
        <h1>NEW YORK TIME API</h1>
      </div>
      <div className="container_main">
        {/* esta parte es para el calendario y listas */}
      <div className="left-panel">

        <fieldset>
          <label htmlFor="">Selecciona una opcion de busqueda</label>
          <select name="" id="" onChange={(e)=>{setFilter(e.target.value)}}>
            <option  defaultChecked >Elige un filtro</option>
            <option value="by_list_fecha">Por lista y fecha</option>
            {/* <option value="by_precios">Por precios</option>
            <option value="by_edades">Por edades</option> */}
          </select>
        </fieldset>

        {
          filter === "by_list_fecha" &&
          <Form  method="POST">
            <input type="hidden" name="endpoint" id="" value={"by_list"} />
            <fieldset className="fieldset-calendar">
            <label htmlFor="">Selecciona una lista disponible</label>
            <select name="lista" onChange={()=>{console.log(e.target.value)}}  disabled={listas.length < 1} id="">
            <option defaultChecked  >Elige una lista</option>
            {
              listas.map((e,index)=>(
                <option key={index} value={e.value}>{e.nombre}</option>
              ))
            }
            </select>
            <label htmlFor="ragoBest">Fecha de publicacion</label>
            <input type="date"  required name="rango_fecha" id="ragoBest"  />
            <button type="submit">Buscar</button>
          </fieldset>
        </Form>
        }
        
      </div>
      <div className="middle-panel">
        {
          libros &&
          libros.map((e)=>(
            <div key={e.value}>
              <img src={e.image} alt="" />
              <Link to={"/index/"+e.value}>{e.tittle}</Link>
            </div>
            
          ))
        }
      </div>
      <div className="right-panel bg-black">
        <Outlet/>
      </div>
      </div>
    </>
  );
}

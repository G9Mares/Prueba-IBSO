import React from 'react'
import { LoaderFunctionArgs , LinksFunction} from '@remix-run/node'
import { useLoaderData } from '@remix-run/react'
import styles from "./styles.css?url"

export async function loader(parametros:LoaderFunctionArgs) {
    const {request,params} = parametros
    const requestOptions:RequestInit  = {
        method: "GET",
        redirect: "follow"
      };
      
      const listas = await fetch(`http://127.0.0.1:8000/get_book/${params.id}`, requestOptions)
        .then((response) => response.json())
        .then((result) => {
          return result
        })
        .catch((error) => console.error(error));
      return {libro:listas}
}
export const links:LinksFunction = () => [
    {rel:"stylesheet",href:styles}
  ]
function Libro() {
    const {libro} = useLoaderData()
    console.log(libro)
  return (
    <div className='card-libro'>
        {
            Object.keys(libro).map(e => {
                if (typeof libro[e]  === 'string') {
                    return (
                        <div><strong>{e}</strong> : {libro[e]}</div>
                    )
                }
            })
        }
    </div>
  )
}

export default Libro
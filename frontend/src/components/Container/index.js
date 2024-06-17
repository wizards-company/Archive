import Head from 'next/head'
import Header from '../Header'
import style from './container.module.css'
import CardBook from '../CardBook'
import CardBlog from '../CardBlog'
import Button from '../Button'

export default function Container() {

    return (
        <> 
            
            <CardBlog/>
            <CardBook/>
            
        </>
    )
}
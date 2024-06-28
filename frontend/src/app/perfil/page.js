"use client"
import Container from "@/components/Container"
import { useEffect, useState } from "react"
import BlogTab from "./components/BlogsTab/BlogTab"
import Actions from "./components/Actions/Actions"
import style from "./Perfil.module.css"
import ButtonsContainer from "./components/ButtonsContainer/ButtonsContainer"
import CardBook from "@/components/CardBook"

export default function Perfil() {
  const [profileInfo, setProfileInfo] = useState(null)
  const [selectBtn, setSelectBtn] = useState(0)
  const info = [
    // Remove this code once the backend is done
    {
      id: 0,
      author: "Willy Wonka",
      title: "How to build your own chocolate fabric",
      text: "First you should capture, I mean hire people and pay them a minimum wage, this way you can get the highest profit out their labor",
      stats: {
        likeCount: 16,
        commentCount: 3,
      },
      donnation: [
        {
          bookName: "Book 1",
          bookAuthor: "That guy",
          bookImg: "someurl",
        },
        {
          bookName: "Book 2",
          bookAuthor: "Another guy",
          bookImg: "someurl",
        },
      ],
      saved: [
        {
          bookName: "Book n",
          bookAuthor: "n guy",
          bookImg: "someurl",
        },
        {
          bookName: "Book n+1",
          bookAuthor: "n+1 guy",
          bookImg: "someurl",
        },
      ],
    },
  ]

  useEffect(() => {
    setProfileInfo(info)
  }, [])

  console.log(profileInfo)

  return (
    <Container>
      <div className={style.flexReverse}>
        <Actions />
        <div className={style.contentContainer}>
          <p className={style.username}>Nome de usuário</p>
          <ButtonsContainer setSelectBtn={setSelectBtn} selectBtn={selectBtn} />

          {selectBtn == 0 && <BlogTab profileInfo={profileInfo} />}
          {selectBtn == 1 && <div>a</div>}
          {selectBtn == 2 && <div>b</div>}
        </div>
      </div>
    </Container>
  )
}

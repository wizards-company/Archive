"use client"
import Image from "next/image"
import style from "./BlogPreview.module.css"
import heartOutline from "@/assets/heartoutline.png"
import heart from "@/assets/heart.png"
import comment from "@/assets/comment.png"
import { useState } from "react"

export default function BlogPreview({
  author,
  title,
  likeCount,
  commentCount,
  text,
}) {
  const [liked, setLiked] = useState(false)
  const [likeCounter, setLikeCounter] = useState(likeCount)

  function handleHeartClick() {
    setLiked((prev) => !prev)
    if (liked) {
      setLikeCounter((prev) => prev - 1)
    } else {
      setLikeCounter((prev) => prev + 1)
    }
  }

  return (
    <div className={style.container}>
      <div className={style.flex}>
        <div className={style.imgIcon}></div>
        <div className={style.authorName}>{author}</div>
      </div>
      <h2 className={`${style.mt5} ${style.title}`}>{title}</h2>
      <span className={`${style.mt5} ${style.text}`}>{text}</span>
      <div className={`${style.mt5} ${style.flex}`}>
        <div className={style.flex}>
          <div onClick={handleHeartClick} className={style.heartContainer}>
            <Image src={heartOutline} className={style.heart} />
            {liked && <Image src={heart} className={style.heart} />}
          </div>
          <div className={`${style.ml5}`}>{likeCounter}</div>
        </div>
        <div className={`${style.ml5} ${style.flex}`}>
          <Image src={comment} className={style.comment} />
          <div className={style.ml5}>{commentCount}</div>
        </div>
      </div>
    </div>
  )
}

import style from "./BlogTab.module.css"
import BlogPreview from "@/components/BlogPreview"

export default function BlogTab({ profileInfo }) {
  return (
    <>
      {/* small screens */}
      <div className={style.flexReverse}>
        <div className={style.contentContainer}>
          <div className={style.contentAreaBig}>
            {profileInfo &&
              profileInfo.map((blog) => (
                <BlogPreview
                  key={blog.id}
                  author={blog.author}
                  commentCount={blog.stats.commentCount}
                  likeCount={blog.stats.likeCount}
                  text={blog.text}
                  title={blog.tite}
                />
              ))}
          </div>
        </div>
      </div>
      {/* large screens */}
      <div className={style.contentAreaSmall}>
        {profileInfo &&
          profileInfo.map((blog) => (
            <BlogPreview
              key={blog.id}
              author={blog.author}
              commentCount={blog.stats.commentCount}
              likeCount={blog.stats.likeCount}
              text={blog.text}
              title={blog.tite}
            />
          ))}
      </div>
    </>
  )
}

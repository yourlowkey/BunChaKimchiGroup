import React from 'react'
import "./closeFriend.css"

// eslint-disable-next-line react/prop-types
export default function CloseFriend({user}) {
  return (
    <li className="sidebarFriend">
        <img className='sidebarFriendImg' src={user.profilePicture} alt="" />
        <span className='sidearFriendName'>{user.username}</span>
    </li>
  )
}

// from enum import StrEnum

// from i_texts import texts as t

export type Command =
  | "start"
  | "get_avatars"
  | "get_paired"
  | "get_cute"
  | "get_angry"
  | "send_picture"
  | "admin"

export type PictureCategory =
  | "avatar"
  | "paired_avatars"
  | "cute"
  | "angry"

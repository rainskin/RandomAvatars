import { t } from "deps"
import { Command } from "enums"

const commands: Record<string, Command> = {
  cmd1: "get_avatars",
  cmd2: "get_paired",
  cmd3: "get_cute",
  cmd4: "get_avatars",
  cmd5: "send_picture",
}

class Texts {
  greet = (mention: string) => t("greet").format({ mention })
  greetGroup = t("greet-group").format(commands)
  doesNotWork = t("does-not-work")
  pictureMenuHint = t("picture-menu-hint")
  // waitFor = t("wait-for")
  // joinRequired = t("join-required")
  // askRights = t("ask-rights")
  // adminPanel = t("admin-panel")
  // askPost = t("ask-post")
  // broadcastStart = t("broadcast-start")
  // requiredJoin = t("required-join")
  // disabled = t("disabled")
  // requiredJoinDisabled = this.requiredJoin.format({ link: this.disabled })
  // askChannelPost = t("ask-channel-post")
  // forwardError = t("forward-error")
  // rightsError = t("rights-error")
  // askSign = t("ask-sign")
  // noSigns = t("no-signs")
}

export const texts = new Texts()

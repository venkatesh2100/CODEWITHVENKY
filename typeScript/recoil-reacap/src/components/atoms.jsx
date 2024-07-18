import { atom, selector } from "recoil";

export const networkAtom = atom({
  key: "networkAtom",
  default: 102,
});

export const homeatom = atom({
  key: "homeatom",
  default: 0,
});
export const jobsatom = atom({
  key: "jobsatom",
  default: 0,
});
export const messagesatom = atom({
  key: "messagesatom",
  default: 4,
});
export const notifyatom = atom({
  key: "notifyatom",
  default: 12,
});


export const finalvalue=selector({
  key:"finalvalue",
  value:({get})=>{
    const Networknotifyvalue=get(networkAtom);
    const Jobsvalue=get(jobsatom);
    const Messagesvalue=get(messagesatom);
    const NotificationsValue=get(networkAtom);
    return Networknotifyvalue+ Jobsvalue+NotificationsValue+ Messagesvalue;
  }
})
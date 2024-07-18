import "./App.css";
import { RecoilRoot, useRecoilValue } from "recoil";
import {
  finalvalue,
  jobsatom,
  messagesatom,
  networkAtom,
  notifyatom,
} from "./components/atoms";
import { useMemo } from "react";

function App() {
  return (
    <RecoilRoot>
      <MyApp />
    </RecoilRoot>
  );
}

function MyApp() {
  console.log("HI");
  const Networknotifyvalue = useRecoilValue(networkAtom);
  const NotificationsValue = useRecoilValue(notifyatom);
  const Jobsvalue = useRecoilValue(jobsatom);
  const Messagesvalue = useRecoilValue(messagesatom);

  const FinalNotificationsValue = useRecoilValue(finalvalue);

  // const FinalNotificationsValue = useMemo (() => {
  //   return Networknotifyvalue + NotificationsValue + Jobsvalue + Messagesvalue;
  // }, [Networknotifyvalue, NotificationsValue, Jobsvalue, Messagesvalue]);

  return (
    <>
      <div>
        <button>HOME</button>
        <button>
          My Network({Networknotifyvalue >= 100 ? "99+" : Networknotifyvalue})
        </button>
        <button>Jobs({Jobsvalue})</button>
        <button>Messages({Messagesvalue})</button>
        <button>Notifications({NotificationsValue})</button>
        <button>Me({FinalNotificationsValue})</button>
      </div>
    </>
  );
}

export default App;

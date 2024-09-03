import React, { useEffect, useRef } from "react";
import { ZegoUIKitPrebuilt } from "@zegocloud/zego-uikit-prebuilt";
import { useParams } from "react-router-dom";

const Room = () => {
  const { id } = useParams();
  const meetingContainerRef = useRef(null);

  useEffect(() => {
    const myMeeting = async () => {
      // generate Kit Token
      const appID = 533644526;
      const serverSecret = "38927f1202c037031666196ba8274162";
      const kitToken = ZegoUIKitPrebuilt.generateKitTokenForTest(
        appID,
        serverSecret,
        id,
        Date.now().toString(),
        "CodingMaster"
      );

      // Create instance object from Kit Token.
      const zp = ZegoUIKitPrebuilt.create(kitToken);

      // Start the call
      zp.joinRoom({
        container: meetingContainerRef.current, // Correct reference to the DOM element
        sharedLinks: [
          {
            name: "Personal link",
            url: `http://localhost:5173/room/${id}`,
          },
        ],
        scenario: {
          mode: ZegoUIKitPrebuilt.OneONoneCall, // Correct mode for 1-on-1 calls
        },
      });
    };

    myMeeting();
  }, [id]); // Correct dependency array

  return (
    <div
      className="myCallContainer"
      ref={meetingContainerRef} // Correct ref usage
      style={{ width: "100vw", height: "100vh" }}
    ></div>
  );
};

export default Room;


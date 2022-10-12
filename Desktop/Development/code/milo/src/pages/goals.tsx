import type { NextPage } from "next";
import Head from "next/head";
import { signIn, signOut, useSession } from "next-auth/react";
import { trpc } from "../utils/trpc";

const Goals: NextPage = () => {
    

    return (
        <>
            <AuthShowcase />
            <GoalCard
                goal="Run for 15 min"
                streak="3"
            />
        </>
    )
}
export default Goals;

const AuthShowcase: React.FC = () => {
    const { data: secretMessage } = trpc.auth.getSecretMessage.useQuery();
  
    const { data: sessionData } = useSession();
  
    return (
      <div className="flex flex-col items-center justify-center gap-2">
        {sessionData && (
          <p className="text-2xl text-blue-500">
            Logged in as {sessionData?.user?.name}
          </p>
        )}
        {secretMessage && (
          <p className="text-2xl text-blue-500">{secretMessage}</p>
        )}
        <button
          className="rounded-md border border-black bg-violet-50 px-4 py-2 text-xl shadow-lg hover:bg-violet-100"
          onClick={sessionData ? () => signOut() : () => signIn()}
        >
          {sessionData ? "Sign out" : "Sign in"}
        </button>
      </div>
    );
  };

type GoalCardProps = {
    goal: string;
    streak: string
}

const GoalCard = ({
    goal,
    streak,
}: GoalCardProps) => {
    return (
        <div>
            <h2>{goal}</h2>
            <h2>{streak}</h2>
        </div>
    )
}
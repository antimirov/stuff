-module(p3).
-compile(export_all).
-export([start/1]).



num_fract(1) -> 1;
num_fract(Num) -> num_fract([], Num, round(math:sqrt(Num)), 1).

num_fract(L,_NumOrig,1,Count) -> {Count+1,lists:reverse(lists:sort(L))};
num_fract(L,NumOrig,CurrDiv,Count) ->
    case (NumOrig rem CurrDiv) =:= 0 of
        true ->
            num_fract([CurrDiv,NumOrig div CurrDiv|L], NumOrig, CurrDiv-1, Count+2);
        false ->
            num_fract(L, NumOrig, CurrDiv-1, Count)
    end.



start([Args]) ->

    Num = list_to_integer(Args),

    {NFract, L} = num_fract(Num),
    LF = lists:zip(lists:map(fun num_fract/1,L), L),

    F = fun({{N,_L},_Fract}) ->
            N == 2
        end,

    [{{_,_},LF1}|_] = lists:filter(F, LF),

    io:format("~nInput num: ~p,  NFract: ~p~nList of fractions: ~p~nFract. List:~p~nList2: ~p~n", [Num, NFract, L, LF, LF1]).

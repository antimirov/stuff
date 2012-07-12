-module(p12).
-compile(export_all).
-export([start/1]).


num_fract(1) -> 1;
num_fract(Num) -> num_fract(Num, round(math:sqrt(Num)), 1).

num_fract(_NumOrig,1,Count) -> Count+1;
num_fract(NumOrig,CurrDiv,Count) ->
    case (NumOrig rem CurrDiv) =:= 0 of
        true ->
            num_fract(NumOrig, CurrDiv-1, Count+2);
        false ->
            num_fract(NumOrig, CurrDiv-1, Count)
    end.


find(Target) ->
    find(1,1,Target).

find(CurrentNum, CurrTr, Target) ->
    case (CurrentNum rem 1000) =:= 0 of
        true -> io:format("\rCurrent num:    ~p", [CurrentNum]);
        false -> ok
    end,

    NumFract = num_fract(CurrTr),
    case NumFract > Target of
        true -> {CurrentNum, CurrTr, NumFract};
        false -> 
            Next = CurrentNum+1,
            find(Next, CurrTr+Next, Target)
    end.



start([Args]) ->

    Num = find(list_to_integer(Args)),
    io:format("~n~p~n", [Num]).

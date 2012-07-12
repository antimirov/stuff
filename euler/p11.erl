-module(p11).
-export([start/0]).



calc_horiz(Arr) ->
    calc_horiz(0,0,Arr,{0,[]}).

calc_horiz(X, Y, Arr, Max) when X == 17 ->
    calc_horiz(0, Y+1, Arr, Max);
calc_horiz(_X, Y, _Arr, Max) when Y == 20 ->
    Max;
calc_horiz(X, Y, Arr, {Max,L}) ->
    Prod = array:get(Y*20+X, Arr) *
           array:get(Y*20+X+1, Arr) *
           array:get(Y*20+X+2, Arr) *
           array:get(Y*20+X+3, Arr),
    case Prod > Max of
        true -> NewMax = {Prod, [array:get(Y*20+X, Arr),
           array:get(Y*20+X+1, Arr),
           array:get(Y*20+X+2, Arr),
           array:get(Y*20+X+3, Arr)]};
        false -> NewMax = {Max,L}
    end,
    calc_horiz(X+1,Y,Arr,NewMax).


calc_vert(Arr) ->
    calc_vert(0,0,Arr,{0,[]}).

calc_vert(X, Y, Arr, Max) when Y == 17 ->
    calc_vert(X+1, 0, Arr, Max);
calc_vert(X, _Y, _Arr, Max) when X == 20 ->
    Max;
calc_vert(X, Y, Arr, {Max,L}) ->
    Prod = array:get(Y*20+X, Arr) *
           array:get((Y+1)*20+X, Arr) *
           array:get((Y+2)*20+X, Arr) *
           array:get((Y+3)*20+X, Arr),
    case Prod > Max of
        true -> NewMax = {Prod, [array:get(Y*20+X, Arr),
           array:get((Y+1)*20+X, Arr),
           array:get((Y+2)*20+X, Arr),
           array:get((Y+3)*20+X, Arr)]};
        false -> NewMax = {Max,L}
    end,
    calc_vert(X,Y+1,Arr,NewMax).


calc_diag1(Arr) ->
    calc_diag1(0,0,Arr,{0,[]}).

calc_diag1(X,Y,_Arr,Max) when (X=:=16) and (Y=:=17) -> Max;
calc_diag1(X, Y, Arr, Max) when Y == 17 ->
    calc_diag1(X+1, 0, Arr, Max);
calc_diag1(X, Y, Arr, Max) when X == 17 ->
    calc_diag1(0, Y+1, Arr, Max);
calc_diag1(X,Y,Arr,{Max,L}) -> 
    %io:format("X: ~p, Y: ~p~n",[X,Y]),
    Prod = array:get(Y*20+X, Arr) *
           array:get((Y+1)*20+X+1, Arr) *
           array:get((Y+2)*20+X+2, Arr) *
           array:get((Y+3)*20+X+3, Arr),
    case Prod > Max of
        true -> NewMax = {Prod,[array:get(Y*20+X, Arr),array:get((Y+1)*20+X+1, Arr),array:get((Y+2)*20+X+2, Arr),array:get((Y+3)*20+X+3, Arr)]};
        false -> NewMax = {Max,L}
    end,
    calc_diag1(X,Y+1,Arr,NewMax).
    

calc_diag2(Arr) ->
    calc_diag2(19,0,Arr,{0,[]}).

calc_diag2(X,Y,_Arr,Max) when (X=:=4) and (Y=:=17) -> Max;
calc_diag2(X, Y, Arr, Max) when Y == 17 ->
    calc_diag2(X-1, 0, Arr, Max);
calc_diag2(X, Y, Arr, Max) when X == 3 ->
    calc_diag2(19, Y+1, Arr, Max);
calc_diag2(X,Y,Arr,{Max,L}) -> 
    %io:format("X: ~p, Y: ~p~n",[X,Y]),
    Prod = array:get(Y*20+X, Arr) *
           array:get((Y+1)*20+X-1, Arr) *
           array:get((Y+2)*20+X-2, Arr) *
           array:get((Y+3)*20+X-3, Arr),
    case Prod > Max of
        true -> NewMax = {Prod,[array:get(Y*20+X, Arr),array:get((Y+1)*20+X-1, Arr),array:get((Y+2)*20+X-2, Arr),array:get((Y+3)*20+X-3, Arr)]};
        false -> NewMax = {Max,L}
    end,
    calc_diag2(X,Y+1,Arr,NewMax).




start() -> 
    {ok,Data} = file:read_file("11.dat"),
    {ok,Data2,_} = regexp:gsub(binary_to_list(Data), "\n", " "),
    {ok, Numbers_Str} = regexp:split(Data2, "\ "),

    NumbersL = lists:map(fun erlang:list_to_integer/1, Numbers_Str),
    Numbers = array:from_list(NumbersL),

    MaxH = calc_horiz(Numbers),
    MaxV = calc_vert(Numbers),
    MaxD1 = calc_diag1(Numbers),
    MaxD2 = calc_diag2(Numbers),


    %io:format("~p = ~p~n", [Numbers, array:size(Numbers)]),
    io:format("MaxH = ~w~n", [MaxH]),
    io:format("MaxV = ~w~n", [MaxV]),
    io:format("MaxD left to right, up to bottom = ~w~n", [MaxD1]),
    io:format("MaxD right to left up to bottom = ~w~n", [MaxD2]).

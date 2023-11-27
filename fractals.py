

def get_fractal_status( high, low):

      fractal   =  np.empty(len(low), dtype=object)
      # fractal =  np.empty(len(low))
      # fractal = [[]] *  len(low)

      for i in range (4 , len(low)):

            N = i - 2
            green_fractal_condition =  low[N]  < low[N-1]  and low[N]  <  low[N-2] and low[N]   <  low[N+1] and low[N]   <  low[N+2]
            red_fractal_condition   =  high[N] > high[N-1] and high[N] >  high[N-2] and high[N] >  high[N+1] and high[N] >  high[N+2]

            # fractal[N]  =   [green_fractal_condition, red_fractal_condition]
            if green_fractal_condition  :
                fractal[N] = 'Green'
                # 'Green'

            if red_fractal_condition :
                fractal[N] = 'Red'
                # 'Red'
            else:
                fractal[N] = 'Neutral'

      return fractal

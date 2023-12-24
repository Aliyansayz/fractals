class fractals(heikin_ashi) :

  def __init__(self, refine_list = None):

      self.refine_list = refine_list

  def run_fractals(self, refine_list):

      fractal_status_list = self.get_fractal(self, bar_list )

      return  fractal_status_list


  def get_fractal(self, bar_list, lookback = None):

        symbols  = 0
        values   = 1
        fractal_status_list =  [[]] * len(bar_list[symbols])
        # np.empty(len(bar_list[symbols]), dtype='U10')

        for  symbol , ohlc in enumerate(bar_list[values]):

            open  = ohlc['Open']
            high  = ohlc['High']
            low   = ohlc['Low']
            close = ohlc['Close']

            fractal  =  self.get_fractal_status(high, low)

            if lookback :

               fractal = fractal[-lookback:]

            fractal_status_list[symbol]   =  fractal

        return  fractal_status_list


  def get_fractal_status(self, high, low):

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

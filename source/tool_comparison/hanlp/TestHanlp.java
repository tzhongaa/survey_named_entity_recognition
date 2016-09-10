import com.hankcs.hanlp.HanLP;
import com.hankcs.hanlp.seg.Segment;
import com.hankcs.hanlp.seg.common.Term;

import java.util.List;

public class TestHanlp
{
    public static void main(String []args)
    {
        String[] testCase = new String[]{"我想喝咖啡",
        "我想预订一杯咖啡，请把它送到腾讯大厦A栋101室",
        "请将咖啡送到福田区百贸大厦2楼101室，可以么？",
        "我家的地址是福田区老佛街108号，记住了哈",
        "请把咖啡送到腾讯大厦",
        "请把咖啡送到百贸大厦",
        };
        Segment segment = HanLP.newSegment().enablePlaceRecognize(true);
        for (String sentence : testCase)
        {
            List<Term> termList = segment.seg(sentence);
            System.out.println(termList);
        }
    }
}

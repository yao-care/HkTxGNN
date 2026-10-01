---
layout: default
title: Etofenamate
parent: 僅模型預測 (L5)
nav_order: 345
evidence_level: L5
indication_count: 5
---

# Etofenamate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Etofenamate：從外用 NSAID 到脊椎關節病變易感性

## 一句話總結

Etofenamate 是外用非類固醇消炎藥（NSAID，為 flufenamic acid 的酯類），目前在香港以凝膠、溶液等外用製劑上市。
TxGNN 模型預測它可能對**脊椎關節病變易感性 (Spondyloarthropathy, Susceptibility to)** 有效。
目前**沒有臨床試驗和文獻**支持，僅有模型預測（證據等級 L5）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 脊椎關節病變易感性 (Spondyloarthropathy, Susceptibility to) |
| TxGNN 預測分數 | 99.9996% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Etofenamate 屬於外用 NSAID，一般認為透過抑制 COX 酶、減少前列腺素合成而產生消炎止痛作用。

NSAID 是脊椎關節炎（spondyloarthritis）的標準症狀治療，所以從藥理上看，這個預測方向說得通。不過有三點需要留意：

- 「脊椎關節病變易感性」是遺傳易感性的描述，不是可直接治療的臨床表現，臨床上很難據此設計試驗。
- Etofenamate 是外用或局部製劑，目前沒有資料顯示它能達到足夠的全身暴露量，來影響軸性（脊椎）疾病。
- 模型分數雖高，但只反映知識圖譜中的關聯，不等於療效證據。

同一批預測中，**僵直性脊椎炎 (Ankylosing Spondylitis)**（分數 99.9984%）的臨床意義更明確。口服 NSAID 是該病的一線治療，Etofenamate 最多只能作為局部肌肉骨骼疼痛的輔助用藥。其餘預測（類風濕性血管炎、尾骨過度活動、Hunter-Thompson 型肢中骨發育不良）的機轉關聯薄弱，很可能是知識圖譜的推論假象。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-53359 | FLOGOPROFEN GEL 5% | HIND WING CO LTD |
| HK-52785 | FLOGOPROFEN SOLUTION 5% | HIND WING CO LTD |
| HK-55383 | ORDOFEN GEL 10% | BRIGHT FUTURE PHARMACEUTICALS FACTORY |
| HK-40437 | NISOLON GEL 50MG/G | WILCOME PHARMACEUTICAL CO LTD |
| HK-41266 | SULKY GEL 5% | YUNG SHIN CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

藥物交互作用查詢未找到相關記錄。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測，沒有任何臨床試驗或文獻佐證。
- 排名第一的預測是遺傳易感性術語，不是可治療的臨床表現。
- 外用劑型能否影響軸性疾病沒有資料，且香港仿單的警語與禁忌尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊核准適應症、警語與禁忌症。
- 補充 Etofenamate 的作用機轉資料（可查詢 DrugBank）。
- 把評估重點改放在更具臨床意義的**僵直性脊椎炎**或局部肌肉骨骼疼痛，並查證外用製劑的全身暴露量與相關文獻。
- 若要進一步研究，先檢索 PubMed 與 ClinicalTrials.gov 有無外用 NSAID 用於脊椎關節炎的既有研究。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


---
layout: default
title: Certolizumab Pegol
parent: 中證據等級 (L3-L4)
nav_order: 176
evidence_level: L4
indication_count: 6
---

# Certolizumab Pegol
{: .fs-9 }

證據等級: **L4** | 預測適應症: **6** 個
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

# Certolizumab Pegol：預測新適應症為類風濕性血管炎

## 一句話總結

Certolizumab Pegol（商品名 Cimzia）是一種 PEG 化的抗 TNF-α 生物製劑，在香港已上市。
TxGNN 模型預測它可能對**類風濕性血管炎 (Rheumatoid Vasculitis)** 有效，但目前只有 **1 篇治療性病例報告**，另有多篇病例報告指出此藥可能**誘發**血管炎。
3 個相關臨床試驗登記皆與此適應症無直接關係，證據方向尚不一致。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 類風濕性血管炎 (Rheumatoid Vasculitis) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據文獻，Certolizumab Pegol 是 PEG 化的 Fab' 片段，能中和 TNF-α，且沒有 Fc 區段。TNF-α 是類風濕疾病中血管發炎的可能驅動因子，因此從機轉上阻斷 TNF 是合理的方向。

類風濕性血管炎是類風濕關節炎的血管併發症，兩者共享 TNF 相關的發炎路徑。檢索到的一篇病例報告（2021 年）描述用 Certolizumab Pegol 治療類風濕性血管炎所致的腿部潰瘍，這是目前唯一的正向線索。

不過，抗 TNF 藥物（包括 Certolizumab Pegol）反覆被報告會引起**矛盾性血管炎**，包括皮膚白血球破碎性血管炎、中型血管炎、蕁麻疹性血管炎，以及腎絲球腎炎。因此淨效益的方向尚未釐清。0.998 的 TxGNN 分數只是模型預測，不能抵消這個安全性訊號。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | 尚未招募 | 80 | 風濕病患者接受肩關節置換術前後的免疫抑制劑停用策略，與血管炎治療無關 |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | 不適用 | 完成 | 184 | 類風濕關節炎患者使用 Tocilizumab 的非介入觀察性研究，無血管炎終點 |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | 不適用 | 未知 | 750,000 | 生物製劑治療後新發免疫媒介發炎疾病風險的大型流行病學研究，屬安全性與流行病學性質 |

以上 3 個試驗皆為間接相關（相關性等級 C），沒有任何試驗直接檢驗類風濕性血管炎的療效。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34786446](https://pubmed.ncbi.nlm.nih.gov/34786446/) | 2021 | 病例報告 | JAAD Case Reports | 使用 Certolizumab Pegol 治療類風濕性血管炎所致的腿部潰瘍（唯一的正向線索） |
| [36597972](https://pubmed.ncbi.nlm.nih.gov/36597972/) | 2022 | 世代研究 | RMD Open | 80 名免疫媒介發炎疾病所致葡萄膜炎患者的長期追蹤，評估 Certolizumab Pegol 的效果與安全性（間接相關） |
| [36418084](https://pubmed.ncbi.nlm.nih.gov/36418084/) | 2022 | 回顧 | RMD Open | 比較免疫調節藥物仿單中的感染頻率與類型（安全性背景） |
| [31990069](https://pubmed.ncbi.nlm.nih.gov/31990069/) | 2020 | 病例報告 | J Clin Pharm Ther | 類風濕關節炎患者在 Certolizumab Pegol 治療期間出現低補體性蕁麻疹性血管炎 |
| [28405087](https://pubmed.ncbi.nlm.nih.gov/28405087/) | 2017 | 病例報告 | Proc (Bayl Univ Med Cent) | Certolizumab Pegol 引起白血球破碎性血管炎的藥物反應 |
| [32687015](https://pubmed.ncbi.nlm.nih.gov/32687015/) | 2021 | 病例報告 | Mod Rheumatol Case Rep | 一名類風濕關節炎患者在開始使用 Certolizumab Pegol 後出現急速進行性腎絲球腎炎 |
| [41158918](https://pubmed.ncbi.nlm.nih.gov/41158918/) | 2025 | 病例報告 | Cureus | 血清陰性類風濕關節炎患者改用 Certolizumab Pegol 後出現抗 TNF 相關中型血管炎 |
| [29610119](https://pubmed.ncbi.nlm.nih.gov/29610119/) | 2018 | 世代研究 | Clin Med Res | 單一中心生物製劑相關皮膚不良事件的經驗 |

在 8 篇文獻中，只有 1 篇報告治療用途，其餘多為藥物引起血管炎或相關自體免疫反應的個案，屬於安全性警訊。

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-61805 | CIMZIA SOLUTION FOR INJ 200MG | UCB PHARMA (HONG KONG) LIMITED |
| HK-67262 | CIMZIA SOLUTION FOR INJECTION IN PRE-FILLED PENS 200MG/1ML | UCB PHARMA (HONG KONG) LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

另請注意：上述文獻顯示，Certolizumab Pegol 及其他抗 TNF 藥物有引起矛盾性血管炎與腎絲球腎炎的個案報告。這是把此藥用於血管炎時必須評估的關鍵風險。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 只有 1 篇治療性病例報告支持，沒有直接的臨床試驗，證據等級為 L4。
- 多篇病例報告顯示此藥可能誘發血管炎，淨效益方向不明，因此不宜僅憑模型分數推進。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症，完成安全性初篩。
- 補充 DrugBank 的作用機轉資料。
- 系統性回顧抗 TNF 藥物用於類風濕性血管炎的治療與誘發血管炎的比例，並與 Rituximab 等替代療法比較。
- 設計小型前瞻性研究或登錄型資料收集，明確納入血管炎的緩解與惡化終點。

**其他預測適應症備註：**
- 「發炎性脊椎病變 (Inflammatory Spondylopathy)」與「脊椎疾病 (Vertebral Disease)」有多個已完成的 Phase 3 隨機對照試驗，證據等級為 L1。這些證據實際對應的是中軸型脊椎關節炎，很可能已是多數地區的核准適應症，可能不算真正的老藥新用，需先對照現行仿單確認。
- 「多關節型幼年類風濕性關節炎」有 1 個已完成的開放標示 Phase 3 試驗（n=193），證據等級為 L2，建議列為研究問題，需先確認現行核准狀態。
- 「尾骨過度活動」與「Kummell 病」僅有模型分數，沒有試驗或文獻，也缺乏機轉依據，暫不建議投入資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


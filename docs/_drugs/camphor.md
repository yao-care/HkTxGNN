---
layout: default
title: Camphor
parent: 中證據等級 (L3-L4)
nav_order: 147
evidence_level: L4
indication_count: 10
---

# Camphor
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Camphor（樟腦）：從外用製劑成分到偏頭痛

## 一句話總結

Camphor（樟腦）在香港是多種外用軟膏和乳液的成分，例如 Vicks VapoRub 和 Mentholatum 軟膏。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效。
目前**沒有臨床試驗**，只有 5 篇間接相關的文獻，且沒有一篇直接證明 camphor 治療偏頭痛有效，所以這只是待驗證的研究假說。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。從藥理上推測，camphor 是 TRPV1 促效劑，也調節 TRPA1/TRPM8 通道，這些通道與外用「抗刺激劑」的止痛感覺有關。三叉神經的痛覺傳導也涉及 TRP 通道，因此外用於頭痛的想法有其合理性。

不過這個連結目前只是假設。原適應症沒有記錄，機轉也沒有資料，無法直接比對兩者的關聯。

支持文獻僅有兩篇精油與叢集性頭痛的病例報告。叢集性頭痛不是偏頭痛，精油也不是單獨的 camphor。這些報告甚至指出含樟腦與尤加利精油的牙膏可能誘發頭痛，方向與療效相反。Camphor 口服後有神經毒性與癲癇風險，這一點必須先釐清，才能談後續開發。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

以下文獻多屬間接相關，沒有一篇在偏頭痛患者中測試 camphor。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36404301](https://pubmed.ncbi.nlm.nih.gov/36404301/) | 2022 | RCT | The Journal of Headache and Pain | Erenumab 預防亞洲慢性偏頭痛的 Phase 3 試驗（DRAGON）。與 camphor 無直接關聯，僅為偏頭痛領域的比較背景 |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Review | Z Kinder Jugendpsychiatr Psychother | 1940–50 年代兒童與青少年神經精神藥物治療的歷史分析，屬背景資料 |
| [593588](https://pubmed.ncbi.nlm.nih.gov/593588/) | 1977 | Review | Minerva Medica | 本態性偏頭痛（hemicrania）的治療回顧，無摘要，與 camphor 的關聯不明 |
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case series | Headache | 5 例叢集性頭痛與使用含促痙攣精油的牙膏有關，屬安全性訊號而非療效 |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case report | BMJ Case Reports | 2 例叢集性頭痛與使用含樟腦、尤加利精油的牙膏時間上相關，屬安全性訊號 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-58885 | MENTHOLATUM OINT | Mentholatum (Asia Pacific) Limited |
| HK-58884 | MENTHOLATUM OINT | Mentholatum (Asia Pacific) Limited |
| HK-54063 | KUMMEL OINTMENT | Kwong Tai Pharmacological Trading Co Ltd |
| HK-31313 | DELTAPHOR LOTION | Meyer Pharmaceuticals Ltd |
| HK-55838 | VICKS VAPORUB OINT | Procter & Gamble HK Ltd |

## 安全性考量

安全性資訊請參考原廠仿單。

證據包中沒有可用的警語、禁忌症或藥物交互作用資料，香港衛生署仿單的警語與禁忌症尚待取得。另外，根據證據包的分析，camphor 口服後有已知的神經毒性與癲癇風險。一篇大鼠急性毒性研究（PMID 27955803）也顯示口服高劑量會造成氧化壓力與組織病理變化。任何開發方向都需要先評估這些風險。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻也沒有直接支持 camphor 治療偏頭痛。現有的兩篇病例報告反而顯示精油可能誘發頭痛。
- 作用機轉資料缺漏，安全性資料是阻斷性缺口，因此目前只能停留在研究問題階段。
- 其他預測適應症（偏頭痛相關亞型、勃起功能障礙、肺高壓、雷諾氏病等）同為 L5 或只有無關文獻，也建議 Hold。肺高壓的 20 篇「文獻」是與 CAMPHOR 問卷同名造成的誤配，不能算作證據。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症，完成 S1 安全性篩選。
- 補齊 DrugBank 的作用機轉資料，驗證 TRP 通道與三叉神經痛覺傳導的假說。
- 檢索並評估外用 camphor 或含樟腦複方用於頭痛的臨床研究。
- 釐清外用劑量與神經毒性、癲癇風險的界線，再評估路徑與劑型的相容性。

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


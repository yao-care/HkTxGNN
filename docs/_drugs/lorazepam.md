---
layout: default
title: Lorazepam
parent: 高證據等級 (L1-L2)
nav_order: 462
evidence_level: L2
indication_count: 5
---

# Lorazepam
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Lorazepam：從苯二氮平類鎮靜劑到失眠治療的實證支持

## 一句話總結

Lorazepam 是常用的苯二氮平類（Benzodiazepine）藥物，透過 GABA-A 受體正向調節產生鎮靜安眠作用。TxGNN 模型將「失眠 (Insomnia)」列為其高分預測適應症之一，這其實與臨床既有實務高度一致——目前有 **21 個相關臨床試驗**及 **18 篇文獻**支持，其中包含直接測試 lorazepam 於失眠患者的隨機對照試驗。

> 補充說明：本次 Evidence Pack 同時列出另外 4 個 TxGNN 高分預測（三叉神經腫瘤、reading seizures、orgasm-induced seizures、audiogenic seizures），但其中評分最高的「三叉神經腫瘤」完全無臨床或文獻證據支持，rationale 中也明確指出這極可能是知識圖譜節點鄰近性造成的假陽性。因此本報告以證據等級最高、決策階段最明確的「失眠」為主軸，其餘候選於文末〈其他候選適應症〉一併列出。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（香港未上市，無核准許可證記載） |
| 預測新適應症 | 失眠 (Insomnia) |
| TxGNN 預測分數 | 99.80%（rank 4657） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Lorazepam 是 GABA-A 受體的正向異位調節劑（positive allosteric modulator）。這個機轉會增強中樞神經系統的抑制性訊號，臨床上早已廣泛用於焦慮、鎮靜及安眠等 on-label/off-label 用途。換言之，「失眠」並非一個需要跨機轉推論的新穎再利用假說，而是苯二氮平類藥物本身藥理特性的直接延伸，屬於既有臨床實務證據的系統性彙整，而非投機性預測。

多篇文獻直接支持這個方向：Bonnet & Arand（1999）針對慢性失眠患者每日三次給予 lorazepam 0.5mg 的療效研究，以及 McClure 等人（1988）比較 lorazepam 與 flurazepam 作為安眠藥的雙盲交叉試驗，均顯示 lorazepam 在多項睡眠參數上有正面效果。同時也有 Phase 2/3 臨床試驗（SM-1 複方，內含 lorazepam）針對短暫性失眠患者進行療效與安全性評估，顯示這個適應症方向已有一定程度的臨床開發軌跡。

需注意的是，苯二氮平類藥物用於慢性失眠存在長期使用之依賴性與戒斷風險，多篇文獻聚焦於「如何減少/停用」而非單純療效驗證，這也是本報告建議「Proceed with Guardrails」而非直接「Go」的主要原因。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03331042](https://clinicaltrials.gov/study/NCT03331042) | Phase 3 | 完成 | 85 | SM-1（含 lorazepam 0.5mg）於暫時性失眠 5 小時時差模型中的療效與安全性評估，對比 diphenhydramine+zolpidem 及 diphenhydramine+lorazepam 組合 |
| [NCT02671760](https://clinicaltrials.gov/study/NCT02671760) | Phase 2 | 完成 | 39 | 評估含 lorazepam 之複方藥物對短期失眠患者總睡眠時間的影響 |
| [NCT04396327](https://clinicaltrials.gov/study/NCT04396327) | Phase 2 | 未招募 | 14 | SM-1（含 lorazepam）於 3 小時時差模型中對暫時性失眠的藥效學評估 |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | 未知 | 1400 | 台灣學術醫學中心前瞻性世代研究，評估老年族群使用安眠藥（含苯二氮平類）之風險效益與使用型態 |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | 完成 | 170 | 電子化自我管理介入計畫協助退伍軍人族群減少/停用苯二氮平類藥物（含 lorazepam） |
| [NCT06584513](https://clinicaltrials.gov/study/NCT06584513) | N/A | 招募中 | 470 | 以病人為中心之實證介入，減少老年患者苯二氮平/鎮靜安眠藥使用以提升用藥安全 |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | 終止 | 2 | Gabapentin 治療苯二氮平依賴，反映長期使用族群的戒斷議題 |
| [NCT03405298](https://clinicaltrials.gov/study/NCT03405298) | N/A | 完成 | 44 | 針對老年患者不當使用苯二氮平類藥物之衛教與行為介入計畫 |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | 終止 | 6 | 比較 α2 促效劑與 GABA 促效劑（含苯二氮平類）鎮靜對機械通氣病人睡眠分期與總睡眠時間的影響 |
| [NCT03338764](https://clinicaltrials.gov/study/NCT03338764) | Phase 3 | 撤回 | 0 | 評估複方 SM-1 於暫時性失眠成人患者之療效與安全性（招募為 0，無可用結果） |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | RCT | J Clin Pharmacol | 雙盲交叉試驗顯示 lorazepam 2mg 在多數睡眠參數上優於 flurazepam 30mg |
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Cohort | Int Clin Psychopharmacol | Lorazepam 0.5mg 每日三次治療慢性失眠，改善日間疲勞與壓力症狀 |
| [19514972](https://pubmed.ncbi.nlm.nih.gov/19514972/) | 2009 | 動物實驗 | Drug Delivery | Lorazepam 鼻腔微乳劑於大鼠睡眠誘導模型中的藥效學評估 |
| [35087274](https://pubmed.ncbi.nlm.nih.gov/35087274/) | 2022 | Review | J Multidiscip Healthc | COVID-19 患者失眠（coronasomnia）治療之療效、安全性與藥物交互作用回顧 |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | Med Lett Drugs Ther | 慢性失眠藥物治療總覽 |
| [30625124](https://pubmed.ncbi.nlm.nih.gov/30625124/) | 2018 | Review | Med Lett Drugs Ther | 慢性失眠口服安眠藥物比較表 |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta分析 | Acta Pharm | 鎮靜劑用於老年慢性病患者之劑量、療效與不良反應統合分析 |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Cohort | Sleep Medicine | 大型管理式照護族群中安眠藥處方型態研究 |
| [25453732](https://pubmed.ncbi.nlm.nih.gov/25453732/) | 2014 | Cohort | Clin Ther | 老年重症退伍軍人苯二氮平/鎮靜安眠藥使用之 Choosing Wisely 適當性評估 |
| [40110386](https://pubmed.ncbi.nlm.nih.gov/40110386/) | 2025 | Cohort | Alpha Psychiatry | 中國東部 2015-2021 年苯二氮平類與 Z-drug 處方趨勢分析 |

## 香港上市資訊

目前香港未有 Lorazepam 相關藥物許可證登記（market_status：未上市，許可證數：0）。

## 安全性考量

安全性資訊請參考原廠仿單。（本次查詢未取得 TFDA/HK 仿單警語、禁忌症及 DDI 資料）

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Lorazepam 用於失眠的機轉明確（GABA-A 受體調節），且已有 Phase 2/3 臨床試驗與多篇直接文獻（含 1988、1999 年之對照研究）支持療效，證據等級達 L2。
- 但苯二氮平類藥物長期使用之依賴性、戒斷及老年族群安全性疑慮同樣有大量文獻著墨，需搭配使用指引與監測機制，不宜無限制推廣。

**若要推進需要：**
- 補齊 TFDA/HK 仿單警語與禁忌症資料（目前為 Blocking 等級資料缺口，直接影響安全性初評）
- 補充 DrugBank 完整 MOA 與 DDI 查詢結果
- 針對長期使用/戒斷風險訂定處方指引（如療程上限、老年族群劑量調整）

---

## 其他候選適應症（次要，僅供研究參考）

| 疾病 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 | 備註 |
|------|-----------|---------|---------|------|------|
| Reading seizures | 99.64% | L4 | S1 | Research Question | 反射性癲癇，GABA 機轉理論支持，但無 lorazepam 直接臨床證據 |
| Audiogenic seizures | 99.63% | L4 | S1 | Research Question | 多為戒斷動物模型文獻，非療效證據 |
| Trigeminal nerve neoplasm | 99.87% | L5 | S0 | Hold | 無任何臨床/文獻支持，rationale 判斷極可能為知識圖譜混淆之假陽性 |
| Orgasm-induced seizures | 99.63% | L5 | S0 | Hold | 極罕見反射性癲癇亞型，完全無證據，僅模型預測 |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


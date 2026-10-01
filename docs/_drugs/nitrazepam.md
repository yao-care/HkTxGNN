---
layout: default
title: Nitrazepam
parent: 中證據等級 (L3-L4)
nav_order: 613
evidence_level: L3
indication_count: 3
---

# Nitrazepam
{: .fs-9 }

證據等級: **L3** | 預測適應症: **3** 個
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

# Nitrazepam：從鎮靜安眠（原適應症資料未登載）到睡眠障礙（入睡與維持睡眠困難）

## 一句話總結

Nitrazepam 是苯二氮平類（benzodiazepine）藥物，在香港已上市，但許可證資料未登載原適應症。
TxGNN 模型預測它可能對**睡眠障礙：入睡與維持睡眠困難 (Sleep disorder, initiating and maintaining sleep)** 有效。
目前**無臨床試驗登記**，有 **20 篇文獻**支持這個方向，包含 1 篇雙盲交叉試驗。這很可能是已有的標示內使用（on-label），並非真正的老藥新用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未登載 |
| 預測新適應症 | 睡眠障礙：入睡與維持睡眠困難 (Sleep disorder, initiating and maintaining sleep) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。Nitrazepam 屬苯二氮平類，這類藥物的已知作用是增強 GABA-A 受體的抑制性訊號，產生鎮靜與安眠效果。這與失眠（入睡困難、睡眠維持困難）的治療需求相符，也解釋了模型給出的高分（0.999）。

文獻也支持這個方向。1969 年的雙盲試驗顯示，nitrazepam 作為安眠藥的效果與 butobarbitone 相當。1983 年的試驗則在老年住院病人中比較 nitrazepam 與 triazolam，兩者在睡眠量與睡眠品質上相近。

需要注意的是，原適應症欄位為空，作用機轉也缺漏，這比較像資料不完整，而不是新發現。Nitrazepam 是行之有年的安眠藥，這個預測很可能只是印證既有用途。仍需對照香港衛生署核准的仿單來確認。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

本次僅取得標題、年份與部分摘要，主要發現依現有內容摘要，缺摘要者僅依標題判斷。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [6135296](https://pubmed.ncbi.nlm.nih.gov/6135296/) | 1983 | RCT（雙盲交叉） | Acta Psychiatr Scand | 26 位老年住院病人，nitrazepam 5 mg 與 triazolam 0.25 mg 的睡眠量、品質及精神運動表現無顯著差異 |
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | 臨床研究 | Br Med J | 與 butobarbitone 效果相當；27 例急性過量（最多 80 錠）僅出現嗜睡，作者認為安全有效 |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Review | BMJ Clin Evid | 老年失眠的盛行率與風險因子整理 |
| [238826](https://pubmed.ncbi.nlm.nih.gov/238826/) | 1975 | Review | Drugs | 從睡眠生理與病理角度評估安眠藥的效果 |
| [7725291](https://pubmed.ncbi.nlm.nih.gov/7725291/) | 1995 | Review | Tidsskr Nor Laegeforen | 失眠的分類、診斷與治療新進展 |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | Review | Clin Pharmacokinet | Nitrazepam 的臨床藥物動力學（無摘要，依標題） |
| [1125532](https://pubmed.ncbi.nlm.nih.gov/1125532/) | 1975 | 病例報告 | Br J Psychiatry | Nitrazepam（Mogadon）依賴性（無摘要，依標題） |
| [15089115](https://pubmed.ncbi.nlm.nih.gov/15089115/) | 2004 | 未分類 | CNS Drugs | 安全眠藥的殘留效應（宿醉、日間嗜睡、精神運動與認知受損）與意外風險，且與劑量高度相關 |
| [10804040](https://pubmed.ncbi.nlm.nih.gov/10804040/) | 2000 | 未分類 | Drugs | Zolpidem 的安眠效果與包含 nitrazepam 在內的苯二氮平類相當 |
| [3281819](https://pubmed.ncbi.nlm.nih.gov/3281819/) | 1988 | 未分類 | Drugs | Brotizolam 改善睡眠的效果與 nitrazepam 2.5 及 5 mg 相近 |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-46067 | ALODORM TAB 5MG | VIATRIS HEALTHCARE HONG KONG LIMITED |
| HK-57864 | NITREDON 5 TAB 5MG | DCH AURIGA (HONG KONG) LIMITED - HEALTHCARE DIVISION |
| HK-20882 | NIPA TAB 5MG | JEAN-MARIE PHARMACAL CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 文獻支持 nitrazepam 用於失眠，且已在香港有 3 張許可證上市，但證據多為較舊的回顧與小型研究，沒有已完成的 Phase 3 RCT，因此證據等級為 L3。
- 這個預測較可能是既有適應症，而非新用途，應先確認法規標示。

**使用時須注意的防護重點：**
- 苯二氮平類的依賴與耐受性風險。
- 半衰期長，可能造成隔日殘留鎮靜。
- 老年人的跌倒與認知風險。
- 較新的藥物（如 orexin 拮抗劑 lemborexant）可作為替代選項。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認原適應症、警語與禁忌症。
- 補齊 DrugBank 的作用機轉資料。
- 取得含摘要的完整文獻，重新評估 1983 年雙盲交叉試驗的試驗階段與結果，再決定證據等級。
- 建立老年及長期使用族群的安全性監測計畫。

**其他預測適應症：**
- 「伴有雙相性痙攣及晚期擴散受限的急性腦病變」（分數 99.59%）：僅有圖譜推論，無試驗與文獻，證據等級 L5，決策 **Hold**。
- 「Wernicke-Korsakoff 症候群」（分數 99.31%）：機轉關聯不明確，核心治療為補充 thiamine，證據等級 L5，決策 **Hold**。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


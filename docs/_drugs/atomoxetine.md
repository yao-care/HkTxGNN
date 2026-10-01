---
layout: default
title: Atomoxetine
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
---

# Atomoxetine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Atomoxetine：從注意力不足過動症 (ADHD) 到特定發展障礙

## 一句話總結

Atomoxetine 是選擇性正腎上腺素再吸收抑制劑，原本用於治療 ADHD（此點依據證據包的機轉說明，香港許可證資料未載明適應症）。
TxGNN 模型預測它可能對**特定發展障礙 (Specific Developmental Disorder)** 有效，目前有 **8 個臨床試驗**和 **15 篇文獻**。
真正屬於老藥新用的證據，是自閉症兒童合併 ADHD 症狀的 RCT，而不是單純 ADHD 的試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 特定發展障礙 (Specific Developmental Disorder) |
| TxGNN 預測分數 | 99.998% |
| 證據等級 | L2（證據包原評 L1，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

**證據等級說明：** L1 需要至少 2 個已完成的 Phase 3 RCT，但這裡只有 1 個（NCT00498173，n=60），其餘為 Phase 4 RCT，另有統合分析佐證。依判定規則應為 L2。證據包自己也指出 L1 只靠一個小型 RCT 加統合分析支撐。

## 為什麼這個預測合理？

Atomoxetine 抑制正腎上腺素轉運體 (NET)，提高前額葉的正腎上腺素與多巴胺活性。這與注意力和衝動控制相關，可能適用於多種神經發展疾病。DrugBank 目前沒有提供作用機轉資料，以上說明來自預測理由欄位。

要注意兩點：

- **ADHD 已是核准適應症。** 單純 ADHD 的試驗（如 NCT00510276）不算老藥新用證據。
- **「特定發展障礙」是很寬的分類。** 與老藥新用最相關的是自閉症合併 ADHD 症狀的族群，有 Phase 3 RCT（NCT00498173）和 Phase 4 RCT（NCT00844753）。2019 年的統合分析（PMID 30653855）納入 3 個安慰劑對照 RCT、共 241 名兒童，評估這個族群的療效與安全性。

## 臨床試驗證據

依相關性排序。前兩項與自閉症族群直接相關，其餘多為背景或安全性參考。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00498173](https://clinicaltrials.gov/study/NCT00498173) | Phase 3 | 完成 | 60 | 雙盲安慰劑對照，評估 atomoxetine 對自閉症兒童與青少年 ADHD 症狀的效果（樣本小） |
| [NCT00844753](https://clinicaltrials.gov/study/NCT00844753) | Phase 4 | 完成 | 128 | Atomoxetine、安慰劑與家長管理訓練，用於自閉症譜系合併 ADHD 症狀的兒童 |
| [NCT00380692](https://clinicaltrials.gov/study/NCT00380692) | Phase 4 | 完成 | 97 | 隨機雙盲安慰劑對照，評估 ASD 兒童與青少年的 ADHD 症狀改善 |
| [NCT00510276](https://clinicaltrials.gov/study/NCT00510276) | Phase 4 | 完成 | 445 | 年輕成人 ADHD 的安慰劑對照試驗（屬已核准適應症，僅為背景） |
| [NCT04085172](https://clinicaltrials.gov/study/NCT04085172) | Phase 4 | 完成 | 396 | 主要試驗藥為 guanfacine，atomoxetine 為對照組，族群為 ADHD |
| [NCT00573859](https://clinicaltrials.gov/study/NCT00573859) | Phase 1/2 | 完成 | 27 | 成人 ADHD 吸菸增強機制研究，與發展障礙療效無關 |
| [NCT01470261](https://clinicaltrials.gov/study/NCT01470261) | N/A | 完成 | 1398 | ADHD 藥物長期影響的非介入研究，僅供安全性背景 |
| [NCT05635318](https://clinicaltrials.gov/study/NCT05635318) | N/A | 未知 | 102 | ADHD 的腦波神經回饋輔助治療，未以 atomoxetine 為研究介入 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30653855](https://pubmed.ncbi.nlm.nih.gov/30653855/) | 2019 | 系統性回顧/統合分析 | Autism Research | 3 個安慰劑對照 RCT、241 名自閉症兒童，評估 atomoxetine 治療 ADHD 症狀的療效與安全性 |
| [39701638](https://pubmed.ncbi.nlm.nih.gov/39701638/) | 2025 | 網絡統合分析 | The Lancet Psychiatry | 比較成人 ADHD 藥物、心理與神經刺激介入的療效與可接受性（摘要僅列研究目的） |
| [32946507](https://pubmed.ncbi.nlm.nih.gov/32946507/) | 2020 | 系統性回顧 | PLoS One | 女性 ADHD 藥物治療的處方率與療效性別差異 |
| [27721971](https://pubmed.ncbi.nlm.nih.gov/27721971/) | 2016 | 回顧 | Ther Adv Psychopharmacol | Atomoxetine 用於 ADHD 合併常見共病（含廣泛性發展障礙）的療效 |
| [25545605](https://pubmed.ncbi.nlm.nih.gov/25545605/) | 2015 | 系統性回顧 | J Affect Disord | 兒童雙相情緒障礙的共病盛行率、臨床影響、病因與治療 |
| [35485452](https://pubmed.ncbi.nlm.nih.gov/35485452/) | 2022 | 回溯性世代研究 | Neuropsychopharmacol Rep | 探討成人 ADHD 中影響 atomoxetine 療效的因素 |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | 回顧 | Clin EEG Neurosci | 兒童 ADHD 與學習障礙的定量腦波應用 |
| [39514707](https://pubmed.ncbi.nlm.nih.gov/39514707/) | 2024 | 個案報告 | J Dev Behav Pediatr | 兒童 ADHD 合併焦慮、憂鬱與自殺意念，使用 atomoxetine 與遠距治療的處置 |
| [41332541](https://pubmed.ncbi.nlm.nih.gov/41332541/) | 2025 | 預印本 | bioRxiv | ADHD 青少年白質結構連結的發展偏離，可預測症狀與治療結果 |
| [16232017](https://pubmed.ncbi.nlm.nih.gov/16232017/) | 2005 | 觀察性研究 | Pharmacotherapy | 兒童 ADHD 選用 atomoxetine 的預測因子 |

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張。資料中的劑型與核准適應症欄位為空，僅能從品名判斷為膠囊劑。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67908 | ATOMILL CAPSULES 10MG | CHEMILL PHARMA LIMITED |
| HK-67910 | ATOMILL CAPSULES 25MG | CHEMILL PHARMA LIMITED |
| HK-61814 | APO-ATOMOXETINE CAPSULES 18MG | HIND WING CO LTD |
| HK-62494 | PMS-ATOMOXETINE CAPSULES 18MG | TRENTON-BOMA LTD |
| HK-62492 | PMS-ATOMOXETINE CAPSULES 40MG | TRENTON-BOMA LTD |

## 安全性考量

安全性資訊請參考原廠仿單。香港衛生署仿單的警語與禁忌尚未取得，這是目前的阻斷性資料缺口，需補齊才能進行安全性篩選。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 自閉症合併 ADHD 症狀有 1 個 Phase 3 RCT、2 個 Phase 4 RCT 和 1 篇統合分析支持，方向一致。
- 但 Phase 3 試驗樣本小（n=60），「特定發展障礙」定義過寬，且缺少仿單安全資料，只適合在限定範圍內推進。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌（阻斷性缺口）。
- 從 DrugBank 補上作用機轉與原適應症，並確認香港核准的適應症範圍。
- 把目標族群限縮為自閉症譜系合併 ADHD 症狀，不用泛稱的發展障礙。
- 確認 NCT00498173、NCT00844753、NCT00380692 的結果數據，必要時評估更大型的驗證試驗。

**其他預測適應症：** 抽動症 (Tourette 症候群、暫時性抽動症) 的證據以 ADHD 合併抽動的研究為主，屬「研究問題」階段。其餘預測（如小腦共濟失調）目前只有模型預測，無臨床證據，均為 Hold。

本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


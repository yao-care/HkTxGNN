---
layout: default
title: Ofatumumab
parent: 僅模型預測 (L5)
nav_order: 625
evidence_level: L5
indication_count: 5
---

# Ofatumumab
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

# Ofatumumab：從 B 細胞惡性腫瘤用藥到 CLL/SLL 前生發中心亞型

## 一句話總結

Ofatumumab 是完全人源化的抗 CD20 單株抗體，香港已有 1 張許可證（HK-67210）。
TxGNN 預測它可能對**前生發中心型慢性淋巴球性白血病／小淋巴球淋巴瘤 (pregerminal center CLL/SLL)** 有效。
這個亞型本身沒有任何臨床試驗或文獻，只有母疾病 CLL/SLL 的間接證據可參考。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 前生發中心型 CLL/SLL (pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L4（此亞型本身無直接研究，僅有機轉合理性與母疾病間接證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

**其他預測適應症一覽（供對照）：**

| 排名 | 預測適應症 | 分數 | 證據等級 | 建議 |
|------|-----------|------|---------|------|
| 2 | IGHV 突變型 CLL/SLL | 99.77% | L4 | Research Question |
| 3 | 濾泡性淋巴瘤 (Follicular Lymphoma) | 99.70% | L2 | Research Question |
| 4 | 淋巴球性白血病易感性 | 99.59% | L4 | Hold |
| 5 | CLL/SLL（整體） | 99.55% | L1 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為資料缺口）。根據模型分析，ofatumumab 是抗 CD20 單株抗體，可透過補體依賴性細胞毒殺 (CDC) 與抗體依賴性細胞毒殺 (ADCC) 清除表現 CD20 的 B 細胞。

前生發中心型 CLL/SLL 是 CLL/SLL 的分子／本體論亞型，通常對應未突變的 IGHV，且仍表現 CD20，因此抗 CD20 機轉在理論上適用。

需要注意：
- 這個亞型沒有專屬的試驗或文獻，支持證據都來自母疾病 CLL/SLL。
- TxGNN 分數高達 99.77%，且與 IGHV 突變型亞型的分數完全相同，很可能反映的是母疾病層級的關聯，不是亞型特異性的訊號。
- 若要判斷不同亞型的療效差異，需要另外做亞型分層分析。

---

## 臨床試驗證據

**目前無相關臨床試驗登記**（針對前生發中心型 CLL/SLL 這個亞型）。

以下是母疾病 CLL/SLL 的試驗，僅供間接參考，共 34 筆，這裡列出 10 筆代表性試驗。多數 Phase 3 試驗中 ofatumumab 是對照組，不是主要試驗藥物。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01578707](https://clinicaltrials.gov/study/NCT01578707) | Phase 3 | 完成 | 391 | Ibrutinib vs ofatumumab，用於復發／難治型 CLL/SLL（ofatumumab 為對照組） |
| [NCT02004522](https://clinicaltrials.gov/study/NCT02004522) | Phase 3 | 完成 | 319 | Duvelisib vs ofatumumab 單藥（DUO 試驗，ofatumumab 為對照組） |
| [NCT00824265](https://clinicaltrials.gov/study/NCT00824265) | Phase 3 | 完成 | 365 | 復發型 CLL：ofatumumab 加 FC vs FC 單用 |
| [NCT01313689](https://clinicaltrials.gov/study/NCT01313689) | Phase 3 | 完成 | 122 | 大腫塊、fludarabine 難治型 CLL：ofatumumab vs 醫師選擇的療法 |
| [NCT01039376](https://clinicaltrials.gov/study/NCT01039376) | Phase 3 | 提前終止 | 480 | 復發型 CLL 誘導治療有效後：ofatumumab 維持治療 vs 不再治療 |
| [NCT02049515](https://clinicaltrials.gov/study/NCT02049515) | Phase 3 | 完成 | 99 | DUO 試驗的延伸研究（duvelisib 或 ofatumumab 單藥） |
| [NCT01520922](https://clinicaltrials.gov/study/NCT01520922) | Phase 2 | 完成 | 99 | Ofatumumab 加 bendamustine，用於未治療或復發型 CLL，單臂試驗 |
| [NCT01113632](https://clinicaltrials.gov/study/NCT01113632) | Phase 2 | 完成 | 77 | Ofatumumab 單藥，用於年長或拒用 fludarabine 的未治療 CLL/SLL |
| [NCT01024010](https://clinicaltrials.gov/study/NCT01024010) | Phase 2 | 完成 | 82 | Pentostatin、cyclophosphamide 加 ofatumumab，用於未治療 CLL/SLL |
| [NCT01145209](https://clinicaltrials.gov/study/NCT01145209) | Phase 2 | 完成 | 32 | Ofatumumab 為基礎的誘導化學免疫治療，後接 ofatumumab 鞏固 |

---

## 文獻證據

**目前無相關文獻**（針對前生發中心型 CLL/SLL 這個亞型）。

以下是母疾病 CLL/SLL 及 ofatumumab 機轉的間接文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31512258](https://pubmed.ncbi.nlm.nih.gov/31512258/) | 2019 | RCT（Phase 3 長期追蹤） | Am J Hematol | RESONATE 最終分析：ibrutinib 單藥在復發／難治型 CLL/SLL 的療效優於 ofatumumab（追蹤中位數 65.3 個月） |
| [37138022](https://pubmed.ncbi.nlm.nih.gov/37138022/) | 2023 | 統合分析 | Ann Hematol | 彙整評估含 ofatumumab 與不含 ofatumumab 的治療方案在 CLL 的療效 |
| [25736010](https://pubmed.ncbi.nlm.nih.gov/25736010/) | 2015 | 臨床指引 | J Natl Compr Canc Netw | NCCN CLL/SLL 指引：ofatumumab 等抗 CD20 抗體帶動了有效的化學免疫治療方案 |
| [24925211](https://pubmed.ncbi.nlm.nih.gov/24925211/) | 2015 | Phase 2 | Leuk Lymphoma | Ofatumumab 加 bendamustine，用於曾接受治療的 CLL/SLL |
| [20481657](https://pubmed.ncbi.nlm.nih.gov/20481657/) | 2010 | 藥物回顧 | Drugs | Ofatumumab 可誘導 ADCC 與 CDC，並回顧其在 fludarabine／alemtuzumab 難治型 CLL 的關鍵試驗 |
| [25882470](https://pubmed.ncbi.nlm.nih.gov/25882470/) | 2015 | Review | Expert Rev Hematol | Ofatumumab 對 CD20 低表現的 CLL 細胞有較強的溶解能力 |
| [26566719](https://pubmed.ncbi.nlm.nih.gov/26566719/) | 2015 | Review（安全性） | Expert Opin Drug Saf | Ofatumumab 單用或合併其他藥物，在 CLL（劑量最高 2000 mg）顯示良好的毒性特徵 |
| [23850806](https://pubmed.ncbi.nlm.nih.gov/23850806/) | 2013 | 前臨床／體外研究 | Haematologica | 補體因子 H 衍生片段可增強 ofatumumab 對 CLL 細胞的 CDC 效果 |

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67210 | KESIMPTA SOLUTION FOR INJECTION IN PRE-FILLED PEN 20MG/0.4ML | NOVARTIS PHARMACEUTICALS (HK) LIMITED |

此許可證的品名為預充填注射筆（20mg/0.4mL）。上方試驗多使用靜脈輸注的高劑量方案，劑型與劑量是否相容需另行確認。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗 CD20 單株抗體，透過 CDC／ADCC 清除 B 細胞） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 前生發中心型 CLL/SLL 這個亞型沒有專屬的臨床試驗或文獻，證據等級僅為 L4。高分預測很可能只是反映母疾病 CLL/SLL 的關聯。
- 若要評估整體 CLL/SLL，母疾病的證據等級為 L1（建議 Proceed with Guardrails），但 CLL 是 ofatumumab 已知的核准用途，屬於既有適應症的確認，不算真正的老藥新用。
- 該 L1 判定主要依據 RESONATE 試驗（ofatumumab 為對照組）與 2023 年統合分析，且證據包只提供了 34 筆 CLL/SLL 試驗中的 10 筆、標題有截斷，建議對照完整清單再確認。

**若要推進需要：**
- 香港衛生署仿單的警語與禁忌資料（目前為阻斷性資料缺口，無法進入 S1 安全性篩選）
- 作用機轉 (MOA) 的完整資料（可從 DrugBank 取得）
- 原適應症與香港核准適應症文字（目前皆為空）
- 亞型分層（IGHV 未突變／突變）的療效資料，才能超越 L4
- 確認香港許可劑型（皮下預充填筆）與試驗所用給藥途徑、劑量的相容性

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


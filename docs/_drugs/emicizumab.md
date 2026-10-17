---
layout: default
title: Emicizumab
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Emicizumab：預測新適應症為後天性凝血因子缺乏 (Acquired coagulation factor deficiency)，以後天性血友病 A 為主（證據等級 L5）。原適應症：血友病（hemophilia）、女性帶因者的症狀性血友病"
monitor_inn: "EMICIZUMAB"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "thrombotic thrombocytopenic purpura", "fetal and neonatal alloimmune thrombocytopenia", "flood factor deficiency"]
---

# Emicizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Emicizumab：從血友病到後天性血友病 A（後天性凝血因子缺乏）

## 一句話總結

Emicizumab 是一種雙特異性抗體，原本用於治療血友病（hemophilia）。
TxGNN 模型的首位預測為 pseudo-von Willebrand disease，但該預測完全缺乏臨床證據；本報告改以證據最充分的**後天性凝血因子缺乏 (Acquired coagulation factor deficiency，主要為後天性血友病 A)** 作為重點評估對象，目前有 **20 篇文獻**支持，其中包含 2 項前瞻性試驗（Phase 2 與 Phase 3，皆為單臂開放標示）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 血友病（hemophilia）、女性帶因者的症狀性血友病（香港許可證未收錄適應症文字） |
| 預測新適應症 | 後天性凝血因子缺乏 (Acquired coagulation factor deficiency)，以後天性血友病 A 為主 |
| TxGNN 預測分數 | 99.90%（全體排名第 2678） |
| 證據等級 | L2（僅有單臂、非隨機試驗，未達 L1） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

> 說明：TxGNN 分數最高的前三項預測（pseudo-von Willebrand disease 99.99%、primary release disorder of platelets 99.99%、Glanzmann thrombasthenia 99.98%）分數雖高，但缺乏臨床證據或機轉依據，詳見結論。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未收錄）。根據藥理學資料，emicizumab 是雙特異性抗體，同時結合活化的凝血因子 IX (FIXa) 與因子 X (FX)，取代活化因子 VIII 的輔因子功能，結合親和力 (KD) 分別約為 1.52 μM 與 0.98 μM。

後天性血友病 A 是自體抗體中和內源性因子 VIII 所致的出血疾病，和先天性血友病 A 在功能缺陷上相同（缺乏 FVIII 活性）。Emicizumab 在結構上與 FVIII 無關，一般不會被抗 FVIII 自體抗體中和，因此在機轉上直接且合理。

現有證據包括日本 Phase 3 研究（AGEHA）、德國 Phase 2 研究（GTH-AHA-EMI）、共識建議、比較性世代研究與真實世界資料。

---

## 臨床試驗證據

目前無相關臨床試驗登記（臨床試驗登記庫中未檢索到資料）。不過下列文獻已報告兩項前瞻性試驗（AGEHA、GTH-AHA-EMI）的結果，詳見文獻證據。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | 前瞻性 Phase 3（AGEHA，單臂） | J Thromb Haemost | Emicizumab 預防後天性血友病 A 出血的首個前瞻性研究 |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | 前瞻性研究最終分析 | Thromb Haemost | 納入不適合免疫抑制治療者與長期預防資料 |
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Phase 2（GTH-AHA-EMI，單臂） | Lancet Haematol | 前 12 週預防出血並可延後免疫抑制治療 |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | 共識建議 | Hamostaseologie | GTH-AHA 工作小組的使用建議 |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | 世代研究 | Blood Adv | 2 年追蹤顯示存活獲益，免疫抑制可延後 |
| [38936699](https://pubmed.ncbi.nlm.nih.gov/38936699/) | 2024 | 比較性世代研究 | J Thromb Haemost | 比較 emicizumab 與免疫抑制治療的處置策略 |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | 真實世界回溯性世代 | Blood Adv | 美國 12 個血友病中心 62 名仿單外使用患者 |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Review | J Thromb Haemost | Emicizumab 時代的後天性血友病 A 處置方式 |
| [40683780](https://pubmed.ncbi.nlm.nih.gov/40683780/) | 2025 | Review | Blood Rev | 後天性血友病 A 處置的最新趨勢 |
| [37276345](https://pubmed.ncbi.nlm.nih.gov/37276345/) | 2023 | 病例系列 | Haemophilia | Emicizumab 用於後天性血友病 A 的病例經驗 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65932 | HEMLIBRA SOLUTION FOR INJECTION 60MG/0.4ML | 注射液 | 未提供 |
| HK-65934 | HEMLIBRA SOLUTION FOR INJECTION 30MG/1ML | 注射液 | 未提供 |
| HK-65935 | HEMLIBRA SOLUTION FOR INJECTION 150MG/1ML | 注射液 | 未提供 |
| HK-65933 | HEMLIBRA SOLUTION FOR INJECTION 105MG/0.7ML | 注射液 | 未提供 |

製造商皆為 ROCHE HONG KONG LIMITED。

---

## 安全性考量

- **藥物交互作用**（共 5 筆）：
  - **Anti-inhibitor coagulant complex (aPCC)：重大 (Major)**，併用有血栓性微血管病變與血栓事件風險。
  - Coagulation factor VIIa（重組）：中度。
  - Antihemophilic factor（重組人類因子 VIII）：中度。
  - 藥理標的：凝血因子 IX、凝血因子 X（作用機轉所致）。
- **TTP 的安全訊號**：emicizumab 促進凝血，並有血栓性微血管病變的通報，對 TTP 屬機轉上不適合。
- **檢驗干擾**：emicizumab 會干擾以 aPTT 與一階段凝血試驗為基礎的檢驗，監測時須注意。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**（針對後天性血友病 A）

**理由：**
- 有 Phase 3 與 Phase 2 前瞻性研究及多項世代資料支持，機轉直接合理，但試驗皆為單臂非隨機，故為 L2。
- 其餘預測多為 L5 或機轉不符，建議 Hold：pseudo-von Willebrand disease、血小板釋放障礙、Scott syndrome、膠原受體缺陷、體質性血小板減少、FNAIT 缺乏機轉依據。**TTP** 很可能是偽陽性且有潛在傷害。Glanzmann thrombasthenia 僅有間接文獻（rFVIIa），列為研究問題。「flood factor deficiency」疾病名稱不明確，需先釐清。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認適應症、警語與禁忌症（目前缺漏）。
- 補充詳細的作用機轉資料（DrugBank）。
- 以隨機對照或較大型前瞻性資料確認療效，並比較 emicizumab 與免疫抑制治療。
- 制定血栓風險管理（避免併用 aPCC、謹慎併用 rFVIIa）與檢驗監測計畫。
- 確認香港對後天性血友病 A 仿單外使用的法規與給付路徑。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


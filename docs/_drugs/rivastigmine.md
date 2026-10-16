---
layout: default
title: Rivastigmine
parent: 中證據等級 (L3-L4)
nav_order: 782
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Rivastigmine：預測新適應症為青光眼 (Glaucoma)（證據等級 L4）。原適應症：阿茲海默症（Alzheimer disease）、小腦退化、Pick 氏病等"
monitor_inn: "RIVASTIGMINE"
predicted_indications: ["glaucoma"]
---

# Rivastigmine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Rivastigmine：從阿茲海默症到青光眼

## 一句話總結

Rivastigmine 是一種膽鹼酯酶抑制劑，原本用於阿茲海默症等神經退化性疾病的治療。
TxGNN 模型預測它可能對**青光眼 (Glaucoma)** 有效，
目前**沒有臨床試驗**，僅有 **3 篇文獻**（1 篇動物實驗、2 篇回顧）提供間接支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 阿茲海默症（Alzheimer disease）、小腦退化、Pick 氏病等（香港許可證未載明核准適應症文字） |
| 預測新適應症 | 青光眼 (Glaucoma) |
| TxGNN 預測分數 | 99.27% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥物類別推論，Rivastigmine 是膽鹼酯酶抑制劑（同時抑制乙醯膽鹼酯酶與丁醯膽鹼酯酶），能提高乙醯膽鹼濃度。

在眼部，乙醯膽鹼作用於蕈毒鹼受體，可促進睫狀肌收縮並增加小樑網的房水流出，進而降低眼壓 (IOP)。這與 pilocarpine、physostigmine 等膽鹼類藥物的作用方向相似。

2000 年一項兔子研究顯示，局部使用 Rivastigmine 可降低眼壓，支持此機轉。2024 年的回顧文獻也間接支持膽鹼系統調控眼壓的概念。不過，目前**沒有青光眼患者的人體資料**，TxGNN 高分只是計算預測，並非臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | 前臨床（兔子） | J Ocul Pharmacol Ther | 局部使用 Rivastigmine 可降低正常眼壓兔子的眼壓 |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Review／系統遺傳學分析 | Front Mol Biosci | 回顧膽鹼類藥物降眼壓的機轉，指出現有 M3 受體促效劑有全身性膽鹼副作用限制 |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Review | Expert Opin Ther Pat | 回顧乙醯膽鹼酯酶抑制劑專利，提及輕度抑制 AChE 在阿茲海默症、重症肌無力及青光眼等具治療意義 |

## 香港上市資訊

香港共有 20 張有效單方許可證（無已註銷）。資料中未提供劑型與核准適應症文字，以下列出主要 5 張：

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-43309 | EXELON CAP 3MG | Novartis Pharmaceuticals (HK) Limited |
| HK-56982 | EXELON PATCH 5 (4.6 MG/24H) | Novartis Pharmaceuticals (HK) Limited |
| HK-56983 | EXELON PATCH 10 (9.5 MG/24H) | Novartis Pharmaceuticals (HK) Limited |
| HK-62812 | EXELON PATCH 15 (13.3MG/24H) | Novartis Pharmaceuticals (HK) Limited |
| HK-60937 | RIVASAN CAP 6MG | Sandoz Hong Kong Limited |

## 安全性考量

- **藥物交互作用**：資料庫共有 100 筆交互作用紀錄，其中包含 **Major** 等級的 **Bupropion**；其餘多為 Moderate 等級，例如抗膽鹼藥物（Atropine、Hyoscyamine、Glycopyrronium、Dicyclomine、Trospium）、H2 阻斷劑（Famotidine、Ranitidine、Cimetidine）、Clarithromycin、Levofloxacin、Metronidazole、Loperamide 等。
- **潛在禁忌疾病（來自知識圖譜，非仿單內容）**：癲癇、氣喘、慢性阻塞性肺病、帕金森氏症及錐體外徑疾病（基底核疾病）、心臟傳導疾病（竇房結症候群、房室傳導阻滯）、猝發心臟驟停、活動性消化性潰瘍、泌尿道阻塞、腹瀉性疾病、厭食症等。

完整警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有動物實驗與回顧文獻的間接支持，缺乏任何人體或臨床試驗資料（證據等級 L4）。TxGNN 分數雖高，仍屬計算預測。
- 全身性膽鹼副作用（心跳過慢、支氣管收縮、腸胃道反應）可能限制其使用，且尚缺仿單層級的安全性資料。

**若要推進需要：**
- 補齊作用機轉與仿單警語／禁忌資料
- 評估局部眼用劑型的可行性與眼部安全性（目前香港許可證僅有口服與貼片劑型，無眼用劑型）
- 設計前臨床補充實驗或小型探索性人體研究，驗證降眼壓效果
- 與現有青光眼藥物（如 pilocarpine）比較療效與全身暴露風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


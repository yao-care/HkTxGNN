---
layout: default
title: Lamotrigine
parent: 僅模型預測 (L5)
nav_order: 506
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Lamotrigine：預測新適應症為三叉神經痛 (Trigeminal Neuralgia)（證據等級 L5）。原適應症：癲癇"
monitor_inn: "LAMOTRIGINE"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
---

# Lamotrigine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Lamotrigine：從癲癇到三叉神經痛
{: .text-alpha }

## 一句話總結

Lamotrigine 是一種抗癲癇藥物，原本用於癲癇、部分性癲癇與 Lennox-Gastaut 症候群等。
TxGNN 模型排名第一的預測是「三叉神經腫瘤」，但這項預測缺乏機轉支持，應視為模型假象。
證據最完整的新適應症是**三叉神經痛 (Trigeminal Neuralgia)**，目前有 **2 個臨床試驗**和 **多篇文獻**支持（以下以三叉神經痛為主要評估對象）。

> 說明：預測排名第一的「三叉神經腫瘤」(TxGNN 分數 99.97%) 僅有 2 篇與腫瘤治療無關的三叉神經痛文獻，沒有臨床試驗，也沒有可信的機轉連結，分數高的原因應是圖譜上與三叉神經痛相近。因此本報告把有實際證據的「三叉神經痛」作為主要評估對象，並另列其他預測供參考。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 癲癇（部分性癲癇、Lennox-Gastaut 症候群等；香港許可證資料中未載明核准適應症文字） |
| 預測新適應症 | 三叉神經痛 (Trigeminal Neuralgia)；排名第一的「三叉神經腫瘤」不建議推進 |
| TxGNN 預測分數 | 三叉神經痛 99.89%（三叉神經腫瘤 99.97%） |
| 證據等級 | L2（三叉神經痛）；三叉神經腫瘤為 L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | 三叉神經痛：Proceed with Guardrails；三叉神經腫瘤：Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未收錄）。根據已知藥理，lamotrigine 可阻斷電壓門控鈉通道並抑制麩胺酸釋放，這是抗癲癇藥物的典型作用方式。

三叉神經痛的成因多為血管壓迫三叉神經根，造成局部去髓鞘與異常放電。鈉通道阻斷可減少這種過度興奮的神經放電，與一線藥物 carbamazepine、oxcarbazepine 的機轉相同。歐洲神經學會 (EAN) 2019 年指引將 lamotrigine 列為輔助或替代選項，而非一線用藥。

相對地，「三叉神經腫瘤」的高分很可能來自圖譜上與三叉神經痛的鄰近關係。Lamotrigine 沒有已知的抗腫瘤活性，兩篇檢索到的文獻也都不是在談以 lamotrigine 治療腫瘤。

---

## 臨床試驗證據

以下為三叉神經痛的試驗（三叉神經腫瘤無臨床試驗）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | 完成 | 21 | Lamotrigine 與 carbamazepine 用於三叉神經痛的療效與安全性比較；樣本小，僅支持 Phase 2 等級證據 |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | NA | 完成 | 20 | 雙盲、安慰劑對照的附加治療試驗，評估 lamotrigine 減少發作的效果與安全性；階段未分類且人數少 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | 系統性回顧 | Biomedicines | 彙整三叉神經痛各類藥物的療效與副作用 |
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | 指引 | Eur J Neurol | 歐洲神經學會三叉神經痛處置指引 |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Pract Neurol | 三叉神經痛實務指南，涵蓋診斷與藥物及手術治療 |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Mol Pain | 從病理生理到藥物治療的概覽 |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | carbamazepine 與 oxcarbazepine 有效但副作用多；第三代抗癲癇藥可作為輔助或單一療法 |
| [24297457](https://pubmed.ncbi.nlm.nih.gov/24297457/) | 2013 | 系統性回顧 | Cochrane Database Syst Rev | Lamotrigine 用於慢性神經痛與纖維肌痛，更新未新增研究 |
| [38246671](https://pubmed.ncbi.nlm.nih.gov/38246671/) | 2024 | 文獻回顧 | No Shinkei Geka | carbamazepine 為一線；lamotrigine 等在日本為仿單外使用，亦有效 |
| [11903537](https://pubmed.ncbi.nlm.nih.gov/11903537/) | 2001 | Review | Headache | 抗癲癇藥物於叢集性頭痛與三叉神經痛的應用 |

---

## 其他預測適應症（供參考）

| 預測適應症 | TxGNN 分數 | 證據等級 | 評估 |
|-----------|-----------|---------|------|
| 三叉神經腫瘤 | 99.97% | L5 | 無機轉連結，相關文獻皆為三叉神經痛，不建議推進 |
| 聲音誘發型癲癇 (Audiogenic seizures) | 99.38% | L4 | 僅有動物模型研究，屬原有抗癲癇作用的確認，無新增再利用價值 |
| 進食誘發型癲癇 (Eating seizures) | 99.38% | L4 | 無直接療效證據，且與原有癲癇適應症重疊 |
| 性高潮誘發型癲癇 (Orgasm-induced seizures) | 99.38% | L5 | 無臨床試驗或文獻，僅為模型預測 |

---

## 香港上市資訊

香港共有 20 張有效單方許可證，無已註銷者。核准適應症文字在資料中未提供。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-37451 | LAMICTAL TAB 100MG（GlaxoSmithKline） | 錠劑 | — |
| HK-37452 | LAMICTAL TAB 50MG（GlaxoSmithKline） | 錠劑 | — |
| HK-39443 | LAMICTAL DISPERSIBLE TAB 5MG（GlaxoSmithKline） | 分散錠 | — |
| HK-56609 | LAMOTRIGINE-TEVA 100MG TAB（Teva） | 錠劑 | — |
| HK-57291 | APO-LAMOTRIGINE TAB 100MG（Hind Wing） | 錠劑 | — |

另有 PMS-Lamotrigine、Lamoga、Epsylam DT、Lamotrix、Lamepil 等其他品牌，合計 20 張。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物－疾病關聯，非仿單原文）：焦慮症、神經官能症、情感遲鈍症、肝病、膽囊疾病、血小板減少、嗜中性球減少、顆粒球缺乏症、貧血（含巨球性貧血）、全血球減少、再生不良性貧血、非感染性腦膜炎。
- **藥物交互作用**：資料庫共查得 100 筆。列出的前 20 筆中，中度交互作用包括 Morphine（含脂質體劑型）、Dronabinol、Nabilone、Metoclopramide、Opium、Orlistat；Metformin 為輕度；其餘（如 Omeprazole、Pantoprazole、Doxycycline、Vancomycin 等）等級未知。

香港仿單的警語與禁忌尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails（三叉神經痛）／Hold（三叉神經腫瘤及其他癲癇亞型預測）**

**理由：**
- 三叉神經痛有 1 項已完成的 Phase 2/3 對照試驗（對照 carbamazepine）與 1 項雙盲安慰劑對照試驗，達 L2 證據，且機轉合理；但樣本僅約 20 人，指引僅列為輔助或替代選項。
- 三叉神經腫瘤的高分缺乏機轉與證據支持，不應推進。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症資料，完成安全性篩選（目前為阻斷性資料缺口）
- 補充藥物作用機轉資料
- 設計較大樣本的對照試驗，或系統性彙整 lamotrigine 對三叉神經痛的現有試驗數據
- 針對知識圖譜標示的血液疾病與肝病風險，擬定監測計畫
- 確認三叉神經痛為仿單外使用，並評估其法規路徑
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


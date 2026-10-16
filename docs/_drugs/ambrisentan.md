---
layout: default
title: Ambrisentan
parent: 高證據等級 (L1-L2)
nav_order: 47
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Ambrisentan：預測新適應症為結締組織疾病相關肺動脈高壓（PAH associated with connective tissue disease）（證據等級 L2）。原適應症：肺動脈高壓（pulmonary arterial hypertension）"
---

# Ambrisentan
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Ambrisentan：從肺動脈高壓到結締組織疾病相關肺動脈高壓

## 一句話總結

Ambrisentan 是一種選擇性內皮素 A 受體（ETA）拮抗劑，原本用於治療肺動脈高壓（PAH）。
TxGNN 模型預測的第一名是**肺動靜脈畸形**，但其證據薄弱、機轉上也不合理。
證據最完整的預測方向是**結締組織疾病相關肺動脈高壓（CTD-PAH）**，目前有 **2 個臨床試驗**和 **18 篇文獻**支持。

> 說明：依預測排名，第 1 名為肺動脈畸形（肺動靜脈畸形），但證據僅有 1 篇病例報告，且機轉上不合理。本報告以「預測排名」與「證據強度」並陳，並以證據最完整的 CTD-PAH 作為主要評估對象。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺動脈高壓（pulmonary arterial hypertension） |
| 預測新適應症 | 結締組織疾病相關肺動脈高壓（PAH associated with connective tissue disease） |
| TxGNN 預測分數 | 99.30% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

> 排名第 1 的「肺動靜脈畸形」TxGNN 分數為 99.41%，證據等級 L4，建議決策為 Hold。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。根據已知資訊，ambrisentan 是選擇性內皮素 A 受體拮抗劑，可阻斷內皮素-1 引起的血管收縮與血管重塑，這也是它在 PAH 中發揮療效的基礎。

CTD-PAH（尤其是系統性硬化症）屬於 WHO 第 1 類 PAH，與原適應症同屬一個疾病家族。內皮素介導的血管收縮與重塑在此族群中已有充分記載，因此以 ETA 阻斷治療在機轉上相當合理。需注意的是，CTD-PAH 對治療的反應通常不如特發性 PAH 明顯。

其他預測的合理性不一：

- **先天性心臟病相關 PAH**：機轉合理，有專屬的 ambrisentan 研究（PMID 21371683），但屬於原 PAH 適應症的子群。
- **HIV 相關 PAH**：機轉合理，但僅有小型病例系列和報告。
- **血吸蟲病、慢性溶血性貧血相關 PAH**：生物學上合理，但完全沒有研究，僅有模型預測。
- **肺動靜脈畸形**：屬於結構性血管分流，預期不會對血管擴張型治療有反應；高分很可能來自知識圖譜中與 PAH 的網絡鄰近性。
- **牙周畸形症候群、頭皮稀毛症、多毛症、Dandy-Walker 畸形症候群**：找不到機轉關聯，應視為圖譜假象。其中多毛症可能反映血管擴張劑（如 minoxidil）的副作用關聯；ambrisentan 具致畸性，也不適合用於發育性疾病。

---

## 臨床試驗證據

以下為 CTD-PAH 的臨床試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02290613](https://clinicaltrials.gov/study/NCT02290613) | Phase 2 | 完成 | 38 | 隨機、雙盲、安慰劑對照的概念驗證試驗，探討系統性硬化症邊緣性 PAH 的早期治療（EDITA） |
| [NCT01042158](https://clinicaltrials.gov/study/NCT01042158) | Phase 4 | 完成 | 25 | 36 週單組開放試驗，評估 ambrisentan 併用 tadalafil 於硬皮症相關 PAH 的 6 分鐘步行距離、NYHA 分級與血流動力學 |

排名第 1 的肺動靜脈畸形及其他預測，目前無相關臨床試驗登記。

---

## 文獻證據

以下為 CTD-PAH 的主要文獻（依證據強度挑選）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | 系統性回顧/統合分析 | Intern Emerg Med | 彙整 RCT 中 CTD-PAH 的治療結果（功能分級、存活、6 分鐘步行距離等） |
| [23906950](https://pubmed.ncbi.nlm.nih.gov/23906950/) | 2013 | 臨床試驗統合分析 | BMJ Open | CTD-PAH 的最佳治療尚未確立，彙整臨床試驗資料 |
| [32161055](https://pubmed.ncbi.nlm.nih.gov/32161055/) | 2020 | 臨床研究（事後分析） | Ann Rheum Dis | AMBITION 試驗中，ambrisentan + tadalafil 起始合併治療與單藥比較於 CTD-PAH |
| [28039187](https://pubmed.ncbi.nlm.nih.gov/28039187/) | 2017 | 臨床研究（次族群分析） | Ann Rheum Dis | AMBITION 試驗的 CTD-PAH 次族群分析 |
| [27492539](https://pubmed.ncbi.nlm.nih.gov/27492539/) | 2016 | 次族群分析 | Respir Med | ARIES-E 試驗中 ambrisentan 於 CTD-PAH 的 3 年療效與安全性 |
| [26360334](https://pubmed.ncbi.nlm.nih.gov/26360334/) | 2015 | 臨床研究 | Am J Respir Crit Care Med | Ambrisentan 與 tadalafil 起始合併治療於硬皮症相關 PAH |
| [28425346](https://pubmed.ncbi.nlm.nih.gov/28425346/) | 2017 | 藥物回顧 | Ther Adv Respir Dis | Ambrisentan 已核准用於特發性、遺傳性及結締組織疾病相關 PAH，可改善運動能力與血流動力學 |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | CTD-PAH 治療的最新進展 |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | PAH 的診斷與治療回顧 |
| [22621693](https://pubmed.ncbi.nlm.nih.gov/22621693/) | 2012 | Review | Drugs | CTD-PAH 的治療 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63502 | VOLIBRIS TABLETS 5MG | — | 資料未提供 |
| HK-63503 | VOLIBRIS TABLETS 10MG | — | 資料未提供 |

兩張許可證均為單一成分製劑，狀態有效，持證商為 GlaxoSmithKline Limited。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：充血性心臟衰竭、貧血（含巨球性貧血）、肺靜脈閉塞症。此資料來自知識圖譜，並非仿單內容。
- **藥物交互作用**：共查詢到 100 筆交互作用。其中中度者包括 canagliflozin、dapagliflozin、empagliflozin、ertugliflozin（SGLT2 抑制劑類）、eliglustat、naltrexone；輕度者包括 clarithromycin、miconazole、omeprazole。
- **其他已知考量**（來自預測分析）：胚胎-胎兒毒性（需 REMS 管控）、水腫、肝功能與血液學監測；HIV 族群需留意與抗反轉錄病毒藥物（如含 ritonavir 的處方）的交互作用；溶血性貧血族群需特別留意體液滯留與貧血。

仿單的警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails（針對 CTD-PAH）**

**理由：**
- CTD-PAH 有 1 個已完成的 Phase 2 試驗、1 個已完成的 Phase 4 試驗，以及統合分析、系統性回顧和 AMBITION、ARIES-E 次族群分析支持，機轉合理，證據等級 L2。
- 兩個試驗規模小（n=38、n=25），且 CTD-PAH 的反應通常不如特發性 PAH 強。ambrisentan 本身已在 PAH 適應症內使用，此方向較接近既有適應症的子族群確認。

**各預測方向的建議：**

| 預測適應症 | 證據等級 | 建議 |
|-----------|---------|------|
| CTD 相關 PAH | L2 | Proceed with Guardrails |
| 先天性心臟病相關 PAH | L3 | Research Question |
| HIV 相關 PAH | L3 | Research Question |
| 肺動靜脈畸形 | L4 | Hold |
| 血吸蟲病相關 PAH | L5 | Hold |
| 慢性溶血性貧血相關 PAH | L5 | Hold |
| 牙周畸形症候群、頭皮稀毛症、多毛症、Dandy-Walker 症候群 | L5 | Hold |

**若要推進需要：**
- 取得香港仿單的警語與禁忌症、核准適應症文字（目前缺漏，屬阻擋性資料缺口）
- 補充詳細的作用機轉資料（MOA）
- 針對 CTD-PAH 規劃較大規模、有對照組的研究，並確認與已核准適應症的差異
- 建立胚胎-胎兒毒性的避孕與妊娠檢測管控、水腫與肝功能/血液學監測計畫
- 確認 CTD-PAH 在香港是否已涵蓋於現有核准適應症內
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


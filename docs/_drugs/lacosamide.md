---
layout: default
title: Lacosamide
parent: 中證據等級 (L3-L4)
nav_order: 427
evidence_level: L3
indication_count: 10
---

# Lacosamide
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Lacosamide：原適應症資料缺失 → 預測新適應症候選（雙相情緒障礙躁狂發作等10項）

## 一句話總結

Lacosamide（DrugBank ID: DB06218）目前**未於香港上市**，且原始適應症與作用機轉（MOA）資料均缺失；文獻中多次將其歸類為第三代抗癲癇藥物（AED）。TxGNN 模型針對此藥物產出 **10 項**預測新適應症，排名第一為**雙相情緒障礙躁狂發作 (Manic Bipolar Affective Disorder)**，目前有 **1 個 Phase 3 臨床試驗**（招募中）與 **14 篇文獻**支持，但整體證據等級僅達 **L3**，屬研究假說階段。值得注意的是，本評估包中「偏頭痛 (migraine disorder)」候選證據強度達 L1（有已完成的 Phase 2/3 RCT），是本次所有預測中證據最紮實的方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（香港未上市，無許可證適應症紀錄；文獻顯示為抗癲癇藥物 AED 類別） |
| 預測新適應症 | 雙相情緒障礙躁狂發作 (Manic Bipolar Affective Disorder) |
| TxGNN 預測分數 | 99.96%（模型排名第 1259 位） |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question |

## 為什麼這個預測合理？

目前缺乏 Lacosamide 詳細的作用機轉資料（DrugBank MOA 欄位為空，列為資料缺口 DG002，需查詢 DrugBank API 補齊）。根據文獻背景資訊，Lacosamide 屬第三代抗癲癇藥物，選擇性增強電位門控鈉通道的慢失活（slow inactivation），與 lamotrigine、carbamazepine、valproate 等已用於雙相情緒障礙的鈉通道調節劑屬同一機轉類比（mood stabilizer via voltage-gated Na channel modulation）。

早期觀察性研究曾提示 lacosamide 對癲癇患者的憂鬱與焦慮症狀有正向影響，後續開放性研究進一步顯示其對雙相情緒障礙患者的憂鬱與躁狂症狀均有改善。不過，evidence pack 中的再利用理由也明確指出：**lacosamide 本身尚無此適應症的機轉專屬性驗證，多數證據來自臨床觀察而非機轉研究**，因此機轉關聯目前僅屬合理推論而非已證實路徑。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Phase 3 | 招募中 | 40 | 評估 lacosamide 作為輔助治療加入一/二線藥物，用於雙相情緒障礙 I/II 型中重度憂鬱發作的療效、安全性與耐受性；試驗設計參考先前開放性研究顯示 lacosamide 可改善雙相患者的憂鬱與躁狂症狀，目前尚無結果數據 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | 回溯性對照研究 | Psychiatry Clin Neurosci | 30天觀察，比較 lacosamide 與其他抗癲癇藥物用於無癲癇共病之雙相情緒障礙患者的效果 |
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | 開放性先導試驗 | J Clin Psychopharmacol | 12週開放性先導試驗，評估 lacosamide 治療雙相憂鬱症之療效與安全性 |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | 個案報告 | Acta Biomed | Lacosamide 穩定合併 PTSD 與額顳葉癲癇之情緒障礙個案，機轉為選擇性鈉通道慢失活以延長細胞膜穩定 |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | 個案報告 | Indian J Psychol Med | 雙相情緒障礙合併癲癇患者使用 lacosamide 誘發嗜中性白血球低下之個案（安全性訊號） |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | 前瞻性多中心研究 | Epilepsy Behav | 評估 lacosamide 對局部難治性癲癇患者憂鬱與焦慮症狀的影響 |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | 個案報告 | Cureus | 雙相情緒障礙第一型合併多重共病孕婦患者的複雜臨床處置討論 |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | 回顧文獻 | Ther Drug Monit | 抗癲癇藥物治療藥物監測（TDM）2018年更新，提及 AED 亦用於雙相情緒障礙等其他適應症之背景 |
| [22210279](https://pubmed.ncbi.nlm.nih.gov/22210279/) | 2012 | 回顧文獻 | Adv Drug Deliv Rev | 1990-2011年間核准之新型抗癲癇藥物化學特性回顧，含 lacosamide |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | 機轉回顧 | ACS Chem Neurosci | CRMP2 作為神經退化疾病藥物標靶之機轉回顧研究 |
| [37782796](https://pubmed.ncbi.nlm.nih.gov/37782796/) | 2023 | 機轉研究（間接） | PNAS | Nav 通道結構研究，以 lamotrigine 為例說明雙位點抑制機轉（非直接針對 lacosamide） |

## 香港上市資訊

Lacosamide 目前未於香港上市，無許可證登記資料。

## 安全性考量

安全性資訊請參考原廠仿單。（TFDA 仿單警語/禁忌屬 Blocking 級資料缺口 DG001，尚未取得，需下載官方仿單解析後方能進行 S1 安全性初評。）

## 結論與下一步

**決策：Research Question**

**理由：**
雙相情緒障礙躁狂發作的證據僅達 L3（回溯性對照研究＋開放性先導試驗＋1個招募中 Phase 3 試驗），尚無完成的隨機對照試驗支持療效，不足以立即推進。值得注意的是，本評估包同時預測「偏頭痛 (migraine disorder)」候選，證據等級已達 **L1**（含已完成的 Phase 2/3 RCT 對照 propranolol，及 CGRP 機轉驗證性研究），為本次所有候選中證據最強者，決策狀態已是「Proceed with Guardrails」，建議優先評估此方向。

**若要推進需要：**
- 補齊 TFDA/仿單安全性資料（DG001，Blocking，為 S1 安全性初評前提）
- 取得完整 DrugBank MOA 資料（DG002）
- 等待 NCT07412132（雙相憂鬱發作）完成並公布結果
- 若考慮推進偏頭痛適應症，優先檢視 NCT05851781（已完成，n=600，lacosamide vs propranolol）之正式發表結果
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


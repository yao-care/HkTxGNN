---
layout: default
title: Tetracaine
parent: 僅模型預測 (L5)
nav_order: 737
evidence_level: L5
indication_count: 5
---

# Tetracaine
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

# Tetracaine：從局部麻醉藥到慢性萎縮性肢端皮膚炎

## 一句話總結

> Tetracaine 是一種酯類局部麻醉藥，目前尚未在香港取得藥品許可證。
> TxGNN 模型預測它可能對**慢性萎縮性肢端皮膚炎 (Acrodermatitis Chronica Atrophicans)** 有效，
> 但目前**沒有臨床試驗、也沒有文獻**支持這個方向，僅為模型預測分數。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無登記資料（evidence pack 未提供） |
| 預測新適應症 | 慢性萎縮性肢端皮膚炎 (Acrodermatitis Chronica Atrophicans) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據一般藥理學已知資訊，Tetracaine 屬於酯類局部麻醉藥（ester-type local anesthetic），常見用於皮膚表面麻醉、黏膜麻醉與眼科局部麻醉，作用機轉主要為阻斷神經細胞膜上的電壓依賴型鈉離子通道，抑制動作電位傳導以達到止痛效果。

慢性萎縮性肢端皮膚炎（Acrodermatitis Chronica Atrophicans, ACA）是一種與萊姆病（Lyme borreliosis, *Borrelia* 感染）相關的慢性皮膚病變，臨床上常伴隨神經病變性疼痛（neuropathic pain）症狀。理論上，若病灶區域有慢性疼痛表現，局部麻醉藥可能有輔助症狀緩解的角色；但這僅為機轉上的推測，evidence pack 中並未提供支持此適應症的作用機轉文獻或臨床資料，因此此關聯性目前**無法驗證**。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

Tetracaine 目前未在香港取得藥品許可證（`total_licenses: 0`），無登記資料可列出。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測適應症（Acrodermatitis Chronica Atrophicans）目前**完全沒有臨床試驗或文獻佐證**，僅有 TxGNN 模型分數（rank 1921），證據等級為 L5。
- 藥物尚未在香港上市，且缺乏 MOA（DG002, High）與仿單警語/禁忌資料（DG001, Blocking），無法進行安全性初評。

**若要推進需要：**
- 補齊仿單警語與禁忌症資料（DG001，Blocking，來源：官方仿單 PDF）
- 查詢 DrugBank API 取得完整作用機轉資料（DG002，High）
- 針對此適應症補充臨床前研究或病例報告等級證據

**補充說明：** Evidence pack 中排名第 5 的候選適應症「acne keloid」證據明顯較充分（已有 1 個 Phase 4 RCT 完成、1 篇相關文獻，內容為 tetracaine 複方乳膏用於雷射治療前局部麻醉），若團隊有意推進 Tetracaine 老藥新用評估，建議優先評估該候選而非本報告的 rank 1 預測。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


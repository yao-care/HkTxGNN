---
layout: default
title: Dextromethorphan
parent: 僅模型預測 (L5)
nav_order: 271
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Dextromethorphan：預測新適應症為鼻腔疾病 (Nasal Cavity Disease)（證據等級 L5）。原適應症：過敏性鼻炎、血管運動性鼻炎、咽炎、感冒、鼻炎、鼻咽炎、頭痛疾患"
monitor_inn: "Dextromethorphan"
predicted_indications: ["faucial diphtheria", "trigeminal autonomic cephalalgia", "cervical disc degenerative disorder", "allergic urticaria"]
---

# Dextromethorphan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Dextromethorphan：從上呼吸道症狀（鼻炎、感冒、咽炎）到鼻腔疾病

## 一句話總結

Dextromethorphan（右美沙芬）是常見的中樞性鎮咳藥，原本用於過敏性鼻炎、血管運動性鼻炎、咽炎、感冒、鼻咽炎等上呼吸道相關症狀。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏性鼻炎、血管運動性鼻炎、咽炎、感冒、鼻炎、鼻咽炎、頭痛疾患（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Dextromethorphan 為單一成分藥物，已用於鼻炎、感冒等上呼吸道症狀，一般認為其鎮咳作用可能與中樞性機轉（如 NMDA 受體拮抗、sigma-1 受體活性）有關，但這些在本次資料中無法驗證。

「鼻腔疾病」是範圍很廣、不具體的疾病分類，與藥物現有的鼻炎、鼻咽炎適應症高度重疊。因此這個高分預測較可能是現有適應症類別的重述，而非真正的新用途。

模型分數雖然很高（99.98%），但反映的是知識圖譜中與既有適應症的鄰近關係，並非新的臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

以下為資料中的 20 張許可證（皆為有效、單一成分），列出其中 5 張。各許可證均未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55879 | NOSPAN TAB 30MG (MALAYSIA) | 未載明 | 未載明 |
| HK-57457 | METHON TAB 30MG | 未載明 | 未載明 |
| HK-67850 | MESUPHY TABLETS 30MG | 未載明 | 未載明 |
| HK-59585 | DEXTROMETHORPHAN SYRUP 15MG/5ML | 未載明 | 未載明 |
| HK-63923 | ANCO TABLETS 30MG | 未載明 | 未載明 |

從品名可見，產品包含錠劑（15 mg、30 mg）、糖漿、酏劑與口服溶液。

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單內容）：高血壓、長 QT 症候群、尖端扭轉型心室頻脈、肝衰竭、肝病、癲癇、慢性阻塞性肺病、支氣管炎、腎臟病、胃潰瘍／消化性潰瘍、胰臟炎、糖尿病（含酮酸中毒）、甲狀腺功能低下、腎上腺皮質功能不足、良性攝護腺增生、血小板低下等。這些來自模型圖譜，需與仿單核對。
- **藥物交互作用**：共記錄 100 筆，其中 Major 等級包括：
  - 血清素相關藥物：Dexfenfluramine、Fenfluramine、Lorcaserin、Sibutramine
  - 5-HT3 拮抗劑：Dolasetron、Granisetron、Ondansetron、Palonosetron
- **中度交互作用**（例）：Bupropion、Morphine、Cimetidine、Metoclopramide、Opium、Phentermine 等。
- 主要警語與正式禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型（L5），沒有臨床試驗或文獻佐證；「鼻腔疾病」過於籠統，且與現有鼻炎類適應症重疊，不構成明確的新用途。
- 作用機轉與香港仿單的警語、禁忌資料皆缺漏，無法進行安全性篩選。

**若要推進需要：**
- 取得 DrugBank 的作用機轉資料，驗證機轉連結
- 下載並解析香港衛生署仿單，補齊警語、禁忌與核准適應症
- 將「鼻腔疾病」具體化為明確的疾病（如特定鼻炎或鼻竇疾病），再進行文獻與試驗檢索
- 評估血清素類與 CYP2D6 相關交互作用的風險管控
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


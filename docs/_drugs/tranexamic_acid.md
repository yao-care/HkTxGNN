---
layout: default
title: Tranexamic Acid
parent: 中證據等級 (L3-L4)
nav_order: 762
evidence_level: L4
indication_count: 1
---

# Tranexamic Acid
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

# TRANEXAMIC ACID：從止血用途到無月經（疑似疾病標籤誤配）

## 一句話總結

> Tranexamic Acid 目前於香港未取得任何藥品許可證，原始適應症資料亦有缺口；已知其臨床用途為抗纖溶止血（減少經期過多出血）。
> TxGNN 模型將其預測連結至**無月經 (Amenorrhea)**，但此方向與藥物已知機轉方向相反，
> 目前僅有 **0 個臨床試驗**和 **2 篇文獻**（且內容談的是「經血過多」而非「無月經」），證據薄弱且疑似節點誤配。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | ⚠️ 資料缺口（未提供結構化欄位；文獻脈絡顯示已知用途為減少經期過多出血/抗纖溶止血） |
| 預測新適應症 | Amenorrhea (無月經) |
| TxGNN 預測分數 | 99.19% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

**目前缺乏詳細的作用機轉資料**（DrugBank MOA 為 Data Gap），但根據已知藥理學常識與本證據包中文獻脈絡可交叉推論：Tranexamic Acid 是抗纖溶藥物，透過抑制 plasminogen 活化來減少出血，臨床上用於治療經血「過多」（menorrhagia / abnormal uterine bleeding），而非誘導或治療「無月經」（amenorrhea）。

本證據包所附的兩篇文獻——〈Pharmacological therapy for abnormal uterine bleeding〉與〈menses prophylaxis and suppression in hematologic cancer patients〉——討論的主題都是「經期出血的管理與抑制」，語意上與「無月經」有部分字面重疊（皆涉及月經調控），但方向並不一致。

**這個預測存在合理性疑慮**：無月經的誘導通常需依賴荷爾蒙抑制排卵的機轉（如 GnRH 類似物、口服避孕藥），並非抗纖溶路徑。高度懷疑 TxGNN 知識圖譜在此將 *amenorrhea* 與 *menorrhagia / abnormal uterine bleeding* 兩個相反概念的疾病節點混淆或錯誤連結。由於 `original_moa` 缺失，目前無法完整交叉驗證，建議先由人工複核疾病標籤正確性，再決定是否推進至下一階段。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause (New York, N.Y.) | 異常子宮出血的藥物治療綜述，涵蓋非荷爾蒙與荷爾蒙藥物選擇依病因、出血量、避孕需求等因素決定 |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | J Oncol Pharm Pract | 血液腫瘤停經前女性病患經期預防與抑制的系統性治療方法，現有藥物比較資料有限 |

⚠️ 兩篇文獻主題均為「經期出血管理／抑制」，與「無月經」的預測方向需進一步釐清關聯性。

---

## 香港上市資訊

Tranexamic Acid 目前尚未於香港取得任何藥品許可證（`market_status`: 未上市，許可證數：0）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：本評估目前缺乏香港仿單警語、禁忌症與藥物交互作用資料（DG001，嚴重度 Blocking），此缺口將阻擋進入 S1 安全性初評階段。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 疾病標籤疑似誤配 — 抗纖溶止血藥物與「無月經」預測方向於機轉上矛盾，附帶文獻主題亦指向相反的臨床情境（經血過多而非無月經）。
- 證據等級僅 L4，無臨床試驗支持，僅 2 篇綜述文獻，且與預測適應症的直接相關性存疑。
- 缺乏 MOA 資料與香港仿單安全性資料，無法進行完整的機轉交叉驗證與 S1 安全性初評。

**若要推進需要：**
- 人工複核 TxGNN 疾病節點標籤，確認 amenorrhea 是否與 menorrhagia / abnormal uterine bleeding 發生混淆（優先事項）
- 補齊 DrugBank MOA 資料以支持機轉關聯性分析（DG002）
- 取得香港仿單警語、禁忌症資料，解除 S1 安全性初評的 Blocking 缺口（DG001）
- 若標籤確認錯誤，建議將此候選自預測清單中排除，並回饋至 TxGNN pipeline 檢查疾病詞彙映射邏輯
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

